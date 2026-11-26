"""Initialize a project from this control-plane release."""

import argparse
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

PACKAGE = Path(__file__).resolve().parents[1]
COMMON = Path("foundation/control-plane")
START = b"<!-- control-plane:start -->"
END = b"<!-- control-plane:end -->"


def saved_bytes(path):
    return path.read_bytes() if path.exists() else None


def lf(data):
    return data.replace(b"\r\n", b"\n")


def collect_files(root):
    return {file.relative_to(root): file.read_bytes() for file in root.rglob("*") if file.is_file()}


def check_path(target, relative):
    path = target
    for part in relative.parts:
        if path.exists() and not path.is_dir():
            raise ValueError(f"路径被文件占用 {path}")
        path /= part
        if path.is_symlink() or (path.exists() and path.resolve() != path):
            raise ValueError(f"目标路径有链接 {path}")
    if path.exists() and not path.is_file():
        raise ValueError(f"需要文件路径 {path}")
    return path


def entrypoint(existing, template):
    if existing is None:
        return template
    if START in existing or END in existing:
        start, end = existing.find(START), existing.find(END)
        if start < 0 or end <= start or existing.count(START) != 1 or existing.count(END) != 1:
            raise ValueError("AGENTS.md 的控制面标记不完整")
        return existing
    newline = b"\r\n" if b"\r\n" in existing else b"\n"
    extra = template.replace(b"\n", newline)
    separator = newline if existing.endswith(newline) else newline + newline
    return existing + separator + extra if existing else extra


def plan(target):
    version_path = COMMON / "VERSION"
    installed = saved_bytes(check_path(target, version_path))
    version = (PACKAGE / "VERSION").read_bytes()
    if installed is not None and lf(installed) != lf(version):
        raise ValueError(f"项目已经使用控制面 {installed.decode('utf-8').strip()}")

    templates = collect_files(PACKAGE / "assets/project")
    common = {
        COMMON / relative: content
        for relative, content in collect_files(PACKAGE / "references/runtime").items()
    }
    assert templates and common
    changes = []
    for relative, desired in sorted({**templates, **common}.items()):
        path = check_path(target, relative)
        existing = saved_bytes(path)
        if relative == Path("AGENTS.md"):
            desired = entrypoint(existing, desired)
        elif existing is not None:
            if relative in templates and installed is not None:
                continue  # Published templates become project-owned files.
            if lf(existing) == lf(desired):
                continue
            raise ValueError(f"已有内容与控制面模板冲突 {relative}")
        if existing != desired:
            changes.append((path, existing, desired))
    if installed is None:
        changes.append((target / version_path, None, version))
    return changes


def replace_file(path, desired):
    with NamedTemporaryFile(dir=path.parent, delete=False) as temp:
        temporary = Path(temp.name)
        try:
            temp.write(desired)
            temp.close()
            os.chmod(temporary, path.stat().st_mode)
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)


def apply(changes):
    created_dirs = []
    written = []
    try:
        for path, existing, desired in changes:
            missing = []
            parent = path.parent
            while not parent.exists():
                missing.append(parent)
                parent = parent.parent
            for folder in reversed(missing):
                folder.mkdir()
                created_dirs.append(folder)
            if existing is None:
                with path.open("xb") as output:
                    written.append((path, None, desired))
                    output.write(desired)
            else:
                if path.read_bytes() != existing:
                    raise ValueError(f"预检后文件发生变化 {path}")
                replace_file(path, desired)
                written.append((path, existing, desired))
    except (OSError, ValueError):
        for path, original, desired in reversed(written):
            current = saved_bytes(path)
            if original is None and current is not None and desired.startswith(current):
                path.unlink()
            elif original is not None and current == desired:
                replace_file(path, original)
        for folder in reversed(created_dirs):
            if not any(folder.iterdir()):
                folder.rmdir()
        raise


def main():
    parser = argparse.ArgumentParser(description="为项目初始化控制面和领域面")
    parser.add_argument("--target", type=Path, required=True, help="已有的项目根目录")
    parser.add_argument("--dry-run", action="store_true", help="只列出拟落地的文件")
    args = parser.parse_args()
    target = args.target.resolve()
    if not target.is_dir():
        parser.error(f"项目目录不存在 {target}")
    try:
        changes = plan(target)
        if not args.dry_run:
            apply(changes)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")
    for path, existing, _ in changes:
        verb = "追加" if existing is not None else "创建"
        print(f"{verb} {path.relative_to(target)}")
    print("无需改动" if not changes else "预检完成" if args.dry_run else "初始化完成")


if __name__ == "__main__":
    main()
