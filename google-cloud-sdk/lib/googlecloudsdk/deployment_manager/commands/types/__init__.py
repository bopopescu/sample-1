# Copyright 2014 Google Inc. All Rights Reserved.

"""Deployment Manager V2 types sub-group."""

from googlecloudsdk.calliope import base


class Types(base.Group):
  """Commands for Deployment Manager V2 types.

  Commands to show available resource types.
  """

  detailed_help = {
      'DESCRIPTION': '{description}',
      'EXAMPLES': """\
          To see the list of all available resource types, run:

            $ {command} list
          """,
  }
