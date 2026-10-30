"""Presentation helpers that preserve canonical machine identifiers."""
import posixpath
import re


def rebase_markdown_links(text, source_dir, target_dir='.'):
    """Reuse generated pages from another directory without breaking file links."""
    def replace(match):
        link=match.group(1)
        if link.startswith(('#','/')) or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',link):
            return match.group(0)
        path,separator,anchor=link.partition('#')
        resolved=posixpath.normpath(posixpath.join(source_dir,path))
        relative=posixpath.relpath(resolved,target_dir)
        return ']('+relative+(separator+anchor if separator else '')+')'
    return re.sub(r'\]\(([^)]+)\)',replace,text)
