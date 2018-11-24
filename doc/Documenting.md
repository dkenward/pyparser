### Whatsnew 

When adding a new feature or fixing a bug, it is much appreciated to document what you did with a compact reference in the whatsnew docs for that version, in <code>doc/source/whatsnew/v<var>X.Y.Z</var>.rst</code> (where <code><var>X.Y.Z</var></code> denotes the current development version of pandas). Please reference the issue or pull request you can do it like so: ``:issue:`12345` `` where `12345` is the issue/pull request number. 

When adding a new feature or fixing a long-standing bug, it is good practice to let users know *when* this feature was added (or bug fixed).

The sphinx syntax for that is:

```rst
.. versionadded:: 0.13.0

Awesome documentation for awesome new feature!
```

This will put the text *New in version 0.13.0* wherever you put the Sphinx directive.

### Release notes

In addition to the whatsnew docs, there are also the release notes. This should not be touched by the contributor in each PR, but this will be written before each release (as the release announcement with a summary of the whatsnew docs, highlights and overview of contributors to this release). 

