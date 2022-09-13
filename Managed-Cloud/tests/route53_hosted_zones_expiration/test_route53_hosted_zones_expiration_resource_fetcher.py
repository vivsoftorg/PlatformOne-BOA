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
import sys
sys.path.append('../../')

from route53_hosted_zones_expiration.route53_hosted_zones_expiration_resource_fetcher import *
from tests.route53_hosted_zones_expiration.test_route53_hosted_zones_expiration_placebo_initializer import *
import common.compliance_object_factory as complianceobjectfactory
import unittest


EVENT_JSON = {
      "configRuleId": "config-rule-1v52mx",
      "version": "1.0",
      "configRuleName": "aws-sample-rule",
      "configRuleArn": "arn:aws:config:us-east-1:107339370656:config-rule/config-rule-1v52mx",
      "invokingEvent": "{\n  \"configurationItemDiff\": null,\n  \"notificationCreationTime\": \"2017-05-19T08:40:15.976Z\",\n  \"messageType\": \"ScheduledNotification\",\n  \"recordVersion\": \"1.2\"\n}",
      "resultToken": "",
      "ruleParameters": "{\"validity\": \"10\", \n \"expirationDateLimit\": \"20\", \n \"notifier\":\"ses\",\n \"toEmail\": \"devendra.suthar@reancloud.com\",\n \"ccEmail\": \"devendra.suthar@reancloud.com\",\n  \"performAction\": \"True\"}",
      "eventLeftScope": "False",
      "executionRoleArn": "arn:aws:iam::107339370656:role/awsconfig-role",
      "accountId": "107339370656"
}

CONTEXT = ""


class TestHostedZonesExpirationFetcher(unittest.TestCase):
    __eventParam = complianceobjectfactory.ComplianceObjectFactory.createEventParamFrom(
        EVENT_JSON,
        CONTEXT
    )

    __hostedZonesFetcher = HostedZoneExpirationResourceFetcher(__eventParam)

    def testWorkSpaceResourceFetcher(self):
        recordedMockResponsePath = PlaceboMockResponseInitializer.getResourceFetcherMock('fetch_hosted_zones')
        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)
        return_value = self.__hostedZonesFetcher.resourceFetcher()
        assert bool(return_value) == True

    def testWorkSpaceResourceFetcherNoData(self):
        recordedMockResponsePath = PlaceboMockResponseInitializer.getResourceFetcherMock('fetch_hosted_zones_blank_response')
        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)
        return_value = self.__hostedZonesFetcher.resourceFetcher()
        assert bool(return_value) == False
