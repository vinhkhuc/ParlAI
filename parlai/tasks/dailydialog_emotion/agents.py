#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
# MODIFIED BY: Vinh Khuc

"""
Daily Dialog
https://arxiv.org/abs/1710.03957

Original data is copyright by the owners of the paper, and free for use in research.

Every conversation contains entries with special fields (see the paper):

- emotion
- act_type
- topic

This teacher plays both sides of the conversation, once acting as Speaker 1, and
once acting as Speaker 2.
"""

from ..dailydialog.agents import DefaultTeacher as DailyDialogDefaultTeacher


# DefaultTeacher is the default one which will be called for the task dailydialog_emotion
class DefaultTeacher(DailyDialogDefaultTeacher):

    def get(self, episode_idx, entry_idx=0):
        # Get original action by DefaultTeacher of DailyDialog
        action = super().get(episode_idx, entry_idx)

        # Move emotion to labels
        emotion = action.pop('emotion')
        action['labels'] = [emotion]
        return action
