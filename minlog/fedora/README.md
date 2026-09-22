# MinLog Fedora review candidate

[minlog.spec](minlog.spec) builds MinLog from the pinned upstream source and runs [MinlogCheck.java](MinlogCheck.java) during `%check`.

The [review release](https://github.com/normlanguage/distribution-packaging/releases/tag/minlog-1.3.1-fedora2) contains the spec, SRPM, binary RPMs, clean Rawhide mock logs, installed-library check and rpmlint report. Rpmlint reports zero errors and one documentation-ratio warning.

The SRPM SHA-256 is `5f41a074c937686afc54a5b94d411c2c60247a3346d30c20e3bff776a07a5264`. Formal Fedora review and acceptance remain pending.

Fedora previously shipped MinLog after [review 919495](https://bugzilla.redhat.com/show_bug.cgi?id=919495). The package was retired on 2019-09-11 after being orphaned for more than six weeks. Because the retirement exceeds eight weeks, restoring it requires a new review before `fedpkg unretire`.
