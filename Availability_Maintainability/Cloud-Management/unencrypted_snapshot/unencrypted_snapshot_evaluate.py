# REANCloud CONFIDENTIAL
# __________________
#
#  (C) 2018 REANCloud LLC
#  All Rights Reserved.
#
# NOTICE: All information contained herein is, and remains
# the property of REANCloud LLC and its suppliers,
# if any. The intellectual and technical concepts contained
# herein are proprietary to REANCloud LLC and its suppliers
# and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from REANCloud LLC.
""" This module will check whether ebs snapshots are encrypted or not, if not then will mark as Non-Compliant."""
from common.abstract_evaluate import AbstractEvaluator
from common.common_constants import ComplianceConstants
from common.logger_utility import LoggerUtility
from common.framework_objects import EvaluationResult
from unencrypted_snapshot.unencrypted_snapshot_constants import SnapshotConstants


class UnencryptedSnapshotEvaluate(AbstractEvaluator):
    """ This class will be responsible for evaluating the resources. """
    def evaluate(self, eventItem):
        try:
            evaluationResult = EvaluationResult()

            if eventItem.configItems[SnapshotConstants.SNAPSHOT_ENCRYPTED]:
                evaluationResult.complianceType = ComplianceConstants.COMPLIANT_RESOURCE
                evaluationResult.annotation = "The snapshot is encrypted"
                self._AbstractEvaluator__evaluatorMessage = evaluationResult.annotation
                LoggerUtility.logInfo("The snapshot {} is encrypted".format(eventItem.resourceId))
                return evaluationResult

            else:
                evaluationResult.complianceType = ComplianceConstants.NON_COMPLIANT_RESOURCE
                evaluationResult.annotation = "The snapshot is not encrypted"
                self._AbstractEvaluator__recommendationMessage = "Please recreate the snapshot & enable encryption on it."
                self._AbstractEvaluator__evaluatorMessage = evaluationResult.annotation
                LoggerUtility.logInfo("The snapshot {} is not encrypted".format(eventItem.resourceId))
                return evaluationResult

        except KeyError as e:
            LoggerUtility.logError(e)
            return False

        except Exception as e:
            LoggerUtility.logError(e)
            return False