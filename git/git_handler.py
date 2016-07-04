#!/usr/bin/python
#
##
##########################################################################
#                                                                        #
#       git_python :: git/git_handler                                    #
#                                                                        #
#       git_python (c) 2015-2016 Vamegh Hedayati                         #
#                                                                        #
#       Vamegh Hedayati <gh_vhedayati AT ev9 DOT io>                     #
#                                                                        #
#       Please see Copying for License Information                       #
#                             GNU/LGPL v2.1 1999                         #
##########################################################################
##
#

import os
import sh
import re
import shutil

class Git_Process(object):
  def __init__(self, clone_path='', remote_repo=''):
    self.path=clone_path
    self.repo=remote_repo
    #self.git = sh.git.bake(_cwd=self.path, _ok_code=[0,1])
    self.git = sh.git.bake(_cwd=self.path)

  def git_clone(self):
    if os.path.isdir(self.path):
      print ("%s already exists - deleting and re-cloning to be safe" % (self.path))
      shutil.rmtree(self.path)
      sh.git.clone(self.repo, self.path)
    else:
      sh.git.clone(self.repo, self.path)

  def git_add(self, add_path=''):
    try:
      print (self.git.add(add_path, _cwd=self.path))
    except sh.ErrorReturnCode_1 as e :
      print ("nothing to add here ... :: Error :: ", e)
      return "fail"

  def git_commit(self, message=''):
    try:
      self.git.commit('-m', message)
    except sh.ErrorReturnCode_1 as e :
      print ("nothing to commit here ... :: Skipping Git Steps :: ")
      return "fail"

  def git_pull(self):
    try:
      print (self.git.pull('--rebase'))
    except sh.ErrorReturnCode_1 as e:
      print ("Cant pull, probably due to uncommited changes :: Error Message :: ", e)
      return "fail"

  def git_push(self):
    try:
      print (self.git.push())
    except sh.ErrorReturnCode_1 as e:
      print ("Cant push, :: Error Message :: ", e)
      return "fail"

  def git_status(self):
    try:
      print (self.git.status)
    except sh.ErrorReturnCode_1 as e:
      print ("Cant get status :: Error Message :: ", e)
      return "fail"

  def git_show(self):
    try:
      print (self.git.show)
    except sh.ErrorReturnCode_1 as e:
      print ("Cant show :: Error Message :: ", e)
      return "fail"

  def git_log(self, commits='2'):
    try:
      print (self.git.log("--decorate=short", "--sparse", "-n", commits))
    except sh.ErrorReturnCode_1 as e:
      print ("Cant show logs ... :: Error Message :: ", e)
      return "fail"

  def __del__(self):
    if os.path.isdir(self.path):
      print ("cleaning up git repo...")
      shutil.rmtree(self.path)

