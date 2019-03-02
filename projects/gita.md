[![PyPi version](https://img.shields.io/pypi/v/gita.svg?color=blue)](https://pypi.org/project/gita/)
[![Build Status](https://travis-ci.org/nosarthur/gita.svg?branch=master)](https://travis-ci.org/nosarthur/gita)
![Codecov](https://img.shields.io/codecov/c/github/nosarthur/gita.svg)
![GitHub contributors](https://img.shields.io/github/contributors/nosarthur/gita.svg)
[![licence](https://img.shields.io/pypi/l/gita.svg)](https://github.com/nosarthur/gita/blob/master/LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/nosarthur/gita.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/nosarthur/gita.svg)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/gita.svg)](https://pypistats.org/packages/gita)

# [gita: a command-line tool to manage multiple git repos](https://github.com/nosarthur/gita)

## purpose

If several repos compile together, it helps to see their status together too. I also hate to change directories to execute git commands.

This tool does two things

- display the status of multiple git repos such as branch, modification, commit message side by side
- delegate git commands/aliases from any working directory

![gita screenshot](https://github.com/nosarthur/gita/raw/master/screenshot.png)

## tech stack

- git
- python
  - argparse
  - subprocess
  - asyncio

## timeline

Currently we don't have big milestones in mind.
Only minor features and bug fixes.

## communication

The preferred way to communicate is using

- github ecosystem

For example, report/fix bugs, request/implement features.
