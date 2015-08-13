#!/usr/local/bin/python

import pygerduty
import sys

#connect to pagerduty with API Key

pager = pygerduty.PagerDuty("<DESC>", "<API>")

#client = sys.argv[1]
client = 'SBS'
#For now we need to manually create the escalation party and grab the ID
escalation = 'PTFV959'
#create generic escalation policy
#pager.escalation_policies.create(name="%s Escalation" % client)

#Create services
pager.services.create(name='%s AlertSite' % client, email_incident_creation='on_new_email_subject', escalation_policy_id=escalation, type="generic_email", service_key= "%s-alertsite" % client.lower(), acknowledgement_timeout=10800, auto_resolve_timeout=43200)

pager.services.create(name='%s Dispatch' % client, email_incident_creation='on_new_email',escalation_policy_id=escalation, type="generic_email", service_key= "%s-dispatch" % client.lower(), acknowledgement_timeout=10800, auto_resolve_timeout=43200)

pager.services.create(name='%s Hyperic' % client, email_incident_creation='only_if_no_open_incidents',escalation_policy_id=escalation, type="generic_email", service_key= "%s-site-alerts" % client.lower(), acknowledgement_timeout=10800, auto_resolve_timeout=43200)

pager.services.create(name='%s Non-Prod' % client, email_incident_creation='on_new_email', escalation_policy_id="PEAQSB8", type="generic_email", service_key= "%s-non-prod" % client.lower() , acknowledgement_timeout=None, auto_resolve_timeout=600)

pager.services.create(name='%s Prod' % client, email_incident_creation='on_new_email', escalation_policy_id="PEAQSB8", type="generic_email", service_key= "%s-prod" % client.lower() , acknowledgement_timeout=None, auto_resolve_timeout=600)

pager.services.create(name='%s Quickbuild' % client,email_incident_creation='on_new_email', escalation_policy_id=escalation, type="generic_email", service_key= "%s-quickbuild" % client.lower(), acknowledgement_timeout=10800, auto_resolve_timeout=43200)

