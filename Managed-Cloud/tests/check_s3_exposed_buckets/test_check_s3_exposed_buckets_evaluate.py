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
import pytest 
import sys
import boto3
from mock import MagicMock
from moto import mock_s3

sys.path.append('../../')

from common.abstract_evaluate import *
import check_s3_exposed_buckets.check_s3_exposed_buckets_evaluate as expBucket
import common.compliance_object_factory as cof
from common.compliance_object_factory import ComplianceObjectFactory
from common.common_constants import *
from common.framework_objects import EvaluationResult

EVENTJSON = {
    "configRuleId": "config-rule-1v52mx",
    "version": "1.0",
    "configRuleName": "aws-sample-rule",
    "configRuleArn": "arn:aws:config:us-east-1:411815166437:config-rule/config-rule-1v52mx",
    "invokingEvent": "{\n  \"configurationItemDiff\": null,\n  \"configurationItem\": {\n    \"relationships\": [],\n    \"configuration\": {\n    \"name\": \"mnc-rean-bucket\",\n    \"owner\": {\n    \"displayName\": \"cloudendure\",\n    \"id\": \"2836b6a0adaf77fc79030606bbda7a5a838e00bf411257a5393eddeb7b4c4cc4\"\n    },\n    \"creationDate\": \"2017-08-23T05: 59: 14.000Z\"\n    },\n    \"supplementaryConfiguration\": {\n    \"AccessControlList\": {\n    \"grantSet\": null,\n    \"grantList\": [\n    {\n    \"grantee\": {\n    \"id\": \"2836b6a0adaf77fc79030606bbda7a5a838e00bf411257a5393eddeb7b4c4cc4\",\n    \"displayName\": \"cloudendure\"\n    },\n    \"permission\": \"FullControl\"\n    },\n    {\n    \"grantee\": \"AllUsers\",\n    \"permission\": \"FullControl\"\n    }\n    ],\n    \"owner\": {\n    \"displayName\": \"cloudendure\",\n    \"id\": \"2836b6a0adaf77fc79030606bbda7a5a838e00bf411257a5393eddeb7b4c4cc4\"\n    },\n    \"isRequesterCharged\": false\n    },\n    \"BucketLoggingConfiguration\": {\n    \"destinationBucketName\": null,\n    \"logFilePrefix\": null\n    },\n    \"BucketPolicy\": {\n    \"policyText\": null\n    },\n    \"BucketAccelerateConfiguration\": {\n    \"status\": null\n    },\n    \"IsRequesterPaysEnabled\": \"false\",\n    \"BucketVersioningConfiguration\": {\n    \"status\": \"Off\",\n    \"isMfaDeleteEnabled\": null\n    },\n    \"BucketNotificationConfiguration\": {\n    \"configurations\": {}\n    }\n    }\n    },\n  \"notificationCreationTime\": \"2017-05-19T08:40:15.976Z\",\n  \"messageType\": \"ConfigurationItemChangeNotification\",\n  \"recordVersion\": \"1.2\"\n}",
    "resultToken": "",
    "eventLeftScope": "False",
    "ruleParameters": "{\n  \"performAction\": \"True\",\n  \"notifier\": \"sns\",\n  \"queueName\": \"gaurav-queue\"\n}",
    "executionRoleArn": "arn:aws:iam::411815166437:role/awsconfig-role",
    "accountId": "411815166437"
}

CONTEXT = ""

eventParam = cof.ComplianceObjectFactory.createEventParamFrom(
    EVENTJSON,
    CONTEXT
)

invalid_invokingEvent = "{\n  \"configurationItemDiff\": null,\n  \"configurationItem\": {\n    \"relationships\": [],\n    \"configuration\": {\n    \"name\": \"mnc-rean-bucket\",\n    \"owner\": {\n    \"displayName\": \"cloudendure\",\n    \"id\": \"2836b6a0adaf77fc79030606bbda7a5a838e00bf411257a5393eddeb7b4c4cc4\"\n    },\n    \"creationDate\": \"2017-08-23T05: 59: 14.000Z\"\n    },\n    \"supplementaryConfiguration\": {\n    \"AccessControlList\": {\n    \"grantSet\": null,\n    \"grantList\":  [\n  {\n    \"grantee\":  {\n    \"id\":  \"2836b6a0adaf77fc79030606bbda7a5a838e00bf411257a5393eddeb7b4c4cc4\",\n     \"displayName\":  \"cloudendure\"\n   },\n    \"permission\":  \"FullControl\"\n   }\n    \n    ],\n     \"owner\": {\n    \"displayName\": \"cloudendure\",\n    \"id\": \"2836b6a0adaf77fc79030606bbda7a5a838e00bf411257a5393eddeb7b4c4cc4\"\n    },\n    \"isRequesterCharged\": false\n    },\n    \"BucketLoggingConfiguration\": {\n    \"destinationBucketName\": null,\n    \"logFilePrefix\": null\n    },\n    \"BucketPolicy\": {\n    \"policyText\": null\n    },\n    \"BucketAccelerateConfiguration\": {\n    \"status\": null\n    },\n    \"IsRequesterPaysEnabled\": \"false\",\n    \"BucketVersioningConfiguration\": {\n    \"status\": \"Off\",\n    \"isMfaDeleteEnabled\": null\n    },\n    \"BucketNotificationConfiguration\": {\n    \"configurations\": {}\n    }\n    }\n    },\n  \"notificationCreationTime\": \"2017-05-19T08:40:15.976Z\",\n  \"messageType\": \"ConfigurationItemChangeNotification\",\n  \"recordVersion\": \"1.2\"\n}"

RESOURCE_TYPE = AWSResourceClassConstants.EC2_INSTANCE
RESOURCE_ID = 'id-as87asd'

class TestS3ExposedBucketEvaluate(object):
    __eventParam = cof.ComplianceObjectFactory.createEventParamFrom(
        EVENTJSON,
        CONTEXT
    )

    __s3ExposedBucketsEvaluate = expBucket.S3ExposedBucketsEvaluate(__eventParam)

    _AbstractEvaluator__eventParam = __eventParam

    @mock_s3
    def test_evaluate_valid_exposed_bucket_acl(self):
        
        evaluationResult = EvaluationResult()
        s3Client = boto3.client('s3', 'us-east-1')
        expBucket.BotoUtility.getClient = MagicMock(return_value=s3Client)
        s3Client.get_bucket_acl = MagicMock(return_value={'Grants': ''})
        eventItem = ComplianceObjectFactory.createAWSConfigEventItemfrom(resourceId=RESOURCE_ID, resourceType=RESOURCE_TYPE, configItems={"name": "test"})
        evaluationResult = expBucket.S3ExposedBucketsEvaluate.evaluate(self, eventItem)

        assert evaluationResult.complianceType == ComplianceConstants.COMPLIANT_RESOURCE

    @mock_s3
    def test_evaluate_exposed_policy_with_invalid_condition_key(self):

        EVENTJSON['invokingEvent'] = invalid_invokingEvent
        eventParam = cof.ComplianceObjectFactory.createEventParamFrom(
            EVENTJSON,
            CONTEXT
        )
        self._AbstractEvaluator__eventParam = eventParam
        s3Client = boto3.client('s3', 'us-east-1')
        expBucket.BotoUtility.getClient = MagicMock(return_value=s3Client)
        s3Client.get_bucket_acl = MagicMock(return_value={'Grants': [
        {
            'Grantee': {
                'DisplayName': 'string',
                'EmailAddress': 'string',
                'ID': 'string',
                'Type': 'CanonicalUser',
                'URI': 'http://acs.amazonaws.com/groups/global/AllUsers'
            },
            'Permission': 'FULL_CONTROL'
        },
    ]})
        # s3Client.get_bucket_policy = MagicMock(return_value="{'Policy': 'Allsers'}")
        eventItem = ComplianceObjectFactory.createAWSConfigEventItemfrom(resourceId=RESOURCE_ID, resourceType=RESOURCE_TYPE, configItems={"name": "test"})
        evaluationResult = EvaluationResult()
        evaluationResult = expBucket.S3ExposedBucketsEvaluate.evaluate(self, eventItem)
        
        assert evaluationResult.complianceType == ComplianceConstants.NON_COMPLIANT_RESOURCE
