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
"""This module will evaluate the events coming from cloudwatch events."""
from common.abstract_evaluate import AbstractEvaluator
from common.framework_objects import EvaluationResult
from common.common_constants import ComplianceConstants
from common.logger_utility import LoggerUtility
from common.i18n import Translation as _


class ProcessCloudwatchEventsEvaluate(AbstractEvaluator):
    """This class will Evaluate the data and makes decision for taking Action."""

    def evaluate(self, eventItem):
        """ perform evaluation for the Cloudwatch events """
        errorMessage = ""
        evaluationResult = EvaluationResult()

        evaluationResult.complianceType = ComplianceConstants.NON_COMPLIANT_RESOURCE
        evaluationResult.annotation = _("This is Sample Annotation for Cloudwatch Event rule")
        LoggerUtility.logInfo(_("This is Sample Annotation for Cloudwatch Event rule"))

        self._AbstractEvaluator__recommendationMessage = "This is Sample Annotation for Cloudwatch Event rule"

        self._AbstractEvaluator__evaluatorMessage = evaluationResult.annotation
        return evaluationResult
