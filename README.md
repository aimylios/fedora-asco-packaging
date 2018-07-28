# Packaging ASCO for Fedora

ASCO is **A** **S**PICE **C**ircuit **O**ptimizer. Please visit the [official ASCO website](http://asco.sourceforge.net/index.html) for details.

As of July 2018, Fedora does not provide an ASCO package but ships the asco binary as part of the (outdated) [qucs-0.0.18](https://src.fedoraproject.org/rpms/qucs) package. To make it easier for me and other Fedora users to use the current version of ASCO, I decided to prepare my own RPM.

This repository only includes the SPEC description file for the ASCO RPM and all of the packaging scripts. The ready-made RPMs are available via my personal [aimylios/electronics](https://copr.fedorainfracloud.org/coprs/aimylios/electronics/) Copr repository.
