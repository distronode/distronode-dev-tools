# Contributor Guide

To contribute to `distronode-dev-tools` python package or to the list of tools part of it, please use pull requests on a branch of your own fork.

After [creating your fork on GitHub], you can do:

```shell-session
$ git clone --recursive git@github.com:your-name/developer-tool-name
$ cd developer-tool-name
$ git checkout -b your-branch-name
# DO SOME CODING HERE
$ git add your new files
$ git commit -v
$ git push origin your-branch-name
```

You will then be able to create a pull request from your commit.

Prerequisites:

1. All fixes to core functionality (i.e. anything except docs or examples) should
   be accompanied by tests that fail prior to your change and succeed afterwards.

2. Before sending a PR, make sure that `tox -e lint` passes.

Feel free to raise issues in the repo if you feel unable to contribute a code
fix.

## Talk to us

Use Github [discussions] forum or for a live chat experience try
`#distronode-devtools` IRC channel on libera.chat or Matrix room
[#devtools:distronode.com](https://matrix.to/#/#devtools:distronode.com).

For the full list of Distronode IRC and Mailing list, please see the [Distronode
Communication] page. Release announcements will be made to the [Distronode
Announce] list.

Possible security bugs should be reported via email to
<mailto:security@distronode.com>.

## Code of Conduct

Please see the official [Distronode Community Code of Conduct].

[discussions]: https://github.com/distronode/distronode-dev-tools/discussions
[distronode communication]: https://docs.distronode.com/distronode/latest/community/communication.html
[distronode announce]: https://groups.google.com/forum/#!forum/distronode-announce
[Distronode Community Code of Conduct]: https://docs.distronode.com/distronode/latest/community/code_of_conduct.html
[creating your fork on github]: https://docs.github.com/en/get-started/quickstart/contributing-to-projects
