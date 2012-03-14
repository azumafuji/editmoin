editmoin
=========

This is a fork of the very nice editmoin package from Gustavo Niemeyer <gustavo@niemeyer.net> from here: http://labix.org/editmoin

The primary changes include a code change to use the optparse packages for the command line options and adding and option to default to trivial change so notifications are not sent by default.  

Our group uses moinmoin for documenting many parallel project and many of the edits do not need to be broadcast so we make most of our edits trivial changes so colleagues are not spammed with change notifications.

How-To
------
To install, run python setup.py install

To see the options to run, editmoin -h

You'll want to set up two files: .moin_aliases and .moin_users

.moin_aliases contains aliases to your wiki like

  <alias> <URI>

The URI in the aliases file should contain any basic auth credentials you may need to access the wiki.

The second file .moin_users sets your account name for the wiki.

  <URI> <username>

The URIs in both files need to match including basic auth credentials.

To make a trivial change use the '-c' flag on the command line.
