# [appengine/14046](https://status.cloud.google.com/incident/appengine/14046)
10:31 Oct 07, 2014
## SUMMARY:
On Saturday 4 October 2014, some Google App Engine applications experienced elevated errors and latency for a period of 3 hours and 4 minutes. We apologize if your application was affected. We know that you depend on Google to provide a reliable service. We are taking steps to prevent a recurrence of this type of incident, and we are crediting all applications in cases where we did not meet the terms of the App Engine Service Level Agreement.
## DETAILED DESCRIPTION OF IMPACT:
On Saturday 4 October 2014 from 09:27 to 12:31 PDT, 8.4% of App Engine applications in US datacenters experienced a rate of serving HTTP 500 errors that was higher than 10%. A further 15% of applications experienced error rates that were lower than 10%. Latency for affected applications was not significantly higher at the median for successful requests. At the 90th percentile, latency increased by 2.2 times. 80% of deployments of new versions failed during the incident period. App Engineâs auto-scaling was impaired during the incident.
## ROOT CAUSE:
The incident occurred after one application made a configuration change that resulted in an invalid state. This state was saved to a storage system used by US applications to store their configuration. Some processes in App Engineâs serving infrastructure received segmentation faults when they tried to read the configuration for this application. Any application that was scheduled to run on a segfaulting server experienced elevated errors and latency.
REMEDIATION AND PREVENTION:
The invalid state was written to storage at 09:27. Our engineers received an automated alert at 09:41, indicating that some processes in one datacenter were failing. We identified the root cause of the problem at 10:35. However, the process that we normally use to write configuration to storage was itself crashing. We therefore had to find an alternative means to repair the configuration. This was completed at 12:14. The new configuration was replicated to all datacenters and the system was stabilized at 12:31.
To prevent recurrence, we will change our code to ensure that an invalid application configuration cannot affect other applications. In addition, we will improve our tools, so that we can repair invalid configurations more quickly.

# [appengine/14049](https://status.cloud.google.com/incident/appengine/14049)
15:12 Oct 28, 2014
## SUMMARY:
On Wednesday 22 October 2014 for a duration of 3 hours 48 minutes, 45.2% of uploads to Google App Engine received incorrect response codes.  Impacted customers can remove orphaned uploads from the Google Developers Console. If uploads to your App Engine application were impacted by this issue, we apologize.  This is not the level of reliability we strive to offer and we are taking immediate steps to improve.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 22 October 2014 from 10:35 to 14:23 PDT, App Engine Blobstore API uploads that had authentication-related fields in their HTTP request headers incorrectly returned HTTP 303, 401 or 403 response codes.  The App Engine upload infrastructure successfully processed the upload requests, but notifications to customer applications did not contain the fields from the original request.
## ROOT CAUSE:
Google Engineers deployed a configuration change on Wednesday 22 October 2014 at 10:35.  This change disabled the forwarding of some authentication-related header fields in the HTTP requests for uploads handled by the Blobstore API.  Requests to POST handlers that required one of these fields failed with HTTP 303, 401 or 403 response codes.
REMEDIATION AND PREVENTION:
At 12:39 Google Cloud Support received multiple customer tickets and informed Google Engineers of an issue with uploads to App Engine applications using the Blobstore API.  We identified the root cause of the issue at 13:29 and began rolling back the change at 13:50.  The rollback was completed at 14:23.
Google engineers are improving App Engineâs release test suite to prevent this issue from recurring.

# [appengine/15001](https://status.cloud.google.com/incident/appengine/15001)
20:47 Jan 21, 2015
## SUMMARY:
On Tuesday 20 January 2015, for a duration of 5 hours 2 minutes, Google App Engine applications using the Channel API experienced a 4.6% error rate in creating new channels. We take this incident very seriously and apologize for any impact it had on your service or application. We have made immediate changes to prevent this issue from recurring.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 20 January 2015 from 10:03 to 15:05 PST, some clients were unable to establish new Channel API sessions. Clients affected by this issue were unable to load the Channel API Javascript library at /_ah/channel/jsapi, and received HTTP 404 âNot Foundâ responses due to an incorrect redirect. Overall, 4.6% of requests to load the relevant client library were affected.
## ROOT CAUSE:
Google engineers began to roll out a new configuration for the service that handles client connections for the Channel API. This new configuration contained an error that caused requests for the Google App Engine Channel API JavaScript client library to redirect to an erroneous location, resulting in an HTTP 404 âNot Foundâ response.
REMEDIATION AND PREVENTION:
Google engineers were alerted to the issue via an external report at 11:49 PST. The engineers identified the configuration changes as the cause of the issue at 13:05. To resolve this issue, the engineers began a rollback of the configuration change at 13:07 which completed at 15:05.
To prevent this type of incident from recurring, Google engineers are adding more thorough monitoring and testing to the configuration deployment process to detect errors of this nature. Google engineers are also tuning the existing monitoring and alerting system to facilitate quicker identification and resolution of elevated error rates.

# [appengine/15002](https://status.cloud.google.com/incident/appengine/15002)
21:10 Jan 21, 2015
## SUMMARY:
On Tuesday 20 January 2015, some Google App Engine applications experienced elevated rates of HTTP 500 errors for a duration of 11 minutes. We apologize if you were affected by this incident. We are working hard to prevent incidents like this from recurring in future.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 20 January 2015, some Google App Engine apps experienced elevated rates of HTTP 500 errors during the following time intervals: 18:24 - 18:27, 18:36 - 18:41, and 19:06 - 19:08 (all times in PST). The issue affected 13% of applications. This issue caused 3% of requests to App Engine to receive 500 errors during the 11 minutes of the incident.
## ROOT CAUSE:
The issue was caused by an error in the software-defined networking control system responsible for network traffic between Google datacenters. The system incorrectly determined that there had been a drop in network capacity available to App Engine applications in one datacenter.
REMEDIATION AND PREVENTION:
Our engineers received an automated alert for the issue at 18:42. At 18:55, we redirected some traffic away from the affected datacenter. The system returned to stability at 19:08.
To prevent a recurrence of this issue, we will disable the subsystem which malfunctioned until both a fix for the immediate malfunction and a defense in depth have been deployed.

# [appengine/15004](https://status.cloud.google.com/incident/appengine/15004)
09:53 Jan 30, 2015
## SUMMARY:
On Wednesday 28 January 2015, some API calls to BigQuery and Cloud Storage returned errors for a duration of 26 minutes. We apologize if your service or application was affected. We are working hard to avoid a recurrence of this type of issue.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 28 January 2015 from 17:01 to 17:27 PST, some API calls to BigQuery and Cloud Storage returned errors. The error rate for BigQuery was 11% during the period of the incident. The error rate for the Cloud Storage XML API was 6%. The error rate for the Cloud Storage JSON API was 12%. The Developers Console returned HTTP 500 errors for 41% of requests for a period of 11 minutes, from 17:01 to 17:12.
## ROOT CAUSE:
The incident resulted from releasing a bad configuration for an internal service, which caused processes to crash. Normally, Google âcanariesâ new releases, by upgrading a small number of servers and looking for problems before releasing the change everywhere. In this case, the canary process failed to operate correctly, causing a large number of processes to crash.
REMEDIATION AND PREVENTION:
Automated monitoring detected the issue and alerted our engineers at 17:02, one minute after the start of the incident. We began rolling back the release at 17:16. The roll back was complete by 17:27.
We are taking several actions to prevent a future recurrence of this type of incident. We have identified the issue that caused processes to crash, and are fixing the issue that caused the canary process to fail.

# [appengine/15005](https://status.cloud.google.com/incident/appengine/15005)
09:47 Feb 25, 2015
## SUMMARY:
On Monday 23 February and Tuesday 24 February 2015, some attempts to deploy new versions of App Engine applications failed for an aggregate period of 356 minutes. We realize that you depend on this service and we apologize if you were affected by this incident. We are taking steps to ensure that incidents of this nature will not happen again.
## DETAILED DESCRIPTION OF IMPACT:
On Monday 23 February, 60% of new version deployment requests failed between 11:00 and 14:15 PST. On Tuesday 24 February 2015, 80% of new version deployment requests failed from 00:05 to 01:47. After that the rate of deployment failures decreased linearly until the incident ended at 02:46.
## ROOT CAUSE:
The App Engine 1.9.18 release required an update to the settings for all applications across the global serving infrastructure. The propagation of this change is handled by Googleâs internal Pub/Sub infrastructure. Posting an update for every one of App Engineâs large number of applications resulted in throttling of messages by this infrastructure. As a result, deployment messages were blocked behind these updates, resulting in timeouts.
REMEDIATION AND PREVENTION:
App Engine began to update application settings  on Monday 23 February at 10:47. The deployment failures began at 11:00. Our engineers detected the problem at 13:06 and we began to investigate the root cause. The incident resolved itself at 14:15.
We then made a further update on Monday 23 February at 23:42. The deployment failures began on Tuesday 24 February at 00:05. Our engineers detected the issue at 01:08, and diagnosed the root cause at 01:11. The Pub/Sub infrastructure's throttle limit was increased at 01:47 and the incident ended at 02:46.
We have now increased App Engineâs throttle limits for the Pub/Sub infrastructure and added an alert to our monitoring systems that will be immediately triggered if this type of event recurs.

# [appengine/15006](https://status.cloud.google.com/incident/appengine/15006)
14:00 Mar 06, 2015
## SUMMARY:
On Thursday 5 March 2015, for a duration of 84 minutes, Google App Engine applications that accessed some Google APIs over HTTP experienced elevated error rates. We apologize for any impact this incident had on your service or application, and have made immediate changes to prevent this issue from recurring.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 5 January, from 07:04 AM to 08:28 AM, some Google App Engine applications making calls to other Google APIs via HTTP experienced elevated error rates. During the incident, the global error rate for all API calls remained under 1%, and in total, the outage affected 2% of applications that were active during the incident.  The effect on those applications was significant: requests to issue OAuth tokens experienced an error rate of over 85%. In addition, the HTTP APIs to googleapis.com/storage and googleapis.com/gmail received error rates between 50% and 60%. Other googleapis.com endpoints were affected with error rates of 10% to 20%.
## ROOT CAUSE:
A component in Googleâs shared HTTP load balancing fabric experienced a non-malicious increase in traffic, exceeding its provisioned capacity. This triggered an automatic DoS protection which shunted a portion of the incoming traffic to a CAPTCHA.  The unexpected response caused some clients to issue automated retries, exacerbating the problem.
REMEDIATION AND PREVENTION:
Google Engineers were alerted to the issue by automated monitoring at 07:02, as the load balancing system detected excess traffic and attempted to automatically mitigate it. At 07:46, Google Engineers enabled standby load balancing capacity to rectify the issue. From 08:15 to 08:40, Google Engineers continued to provision additional resources in the load balancing fabric in order to serve the increased traffic. During this period, at 08:28, Google engineers determined that sufficient capacity was in place to serve both regular and retry traffic, and instructed the load balancing system to cease mitigation and resume normal traffic serving.  This action marked the end of the event.
To prevent this issue from recurring, Google engineers are comprehensively re-examining the affected load balancing fabric to ensure it is and remains correctly provisioned.  Additionally, Google engineers are improving monitoring rules to provide an early warning of capacity shortfall. Finally, Google engineers are examining the services that depend on this load balancing system, and will move some services to a separate pool of more easily scalable load balancers where appropriate.

# [appengine/15007](https://status.cloud.google.com/incident/appengine/15007)
17:28 Mar 11, 2015
## SUMMARY:
On Monday 9 March 2015, deployments of Google App Engine applications running on Beta Managed VMs experienced intermittent deployment failures for a duration of 75 minutes. Whilst Managed VMs is still in Beta, we apologize for any impact this incident may have had on your service or application.
## DETAILED DESCRIPTION OF IMPACT:
Between 18:20 and 19:40 PDT, users of Google App Engine Managed VMs (Beta) experienced intermittent deployment failures. Users impacted by this incident would see gcloud or appcfg deploy commands return with error messages. Over this period, 81% of deployments returned errors.
## ROOT CAUSE:
The Managed VMs (Beta) deployment system relies on the Google Cloud Storage JSON API, which experienced a 5% failure rate during this time period.  For details, see the Cloud Storage incident post: https://status.cloud.google.com/incident/storage/16021.
REMEDIATION AND PREVENTION:
The primary remediation for this incident is described in the Cloud Storage incident report. In addition to the steps outlined there, Google engineers are tuning the systems that monitor Managed VMs application deployments to alert earlier, which will facilitate speedier resolution.

# [appengine/15009](https://status.cloud.google.com/incident/appengine/15009)
22:32 Mar 25, 2015
## SUMMARY:
On Tuesday 24th March 2015, Google App Engine served elevated 503 errors on <1% of applications for a typical duration of 50 minutes.  We know how important high uptime and low error rates are to you and your users, and we apologize for these errors. We are learning from this incident and are implementing several improvements to make our service more reliable.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 24th March 2015 from 13:03 to 13:53 PDT approximately 1% of requests to App Engine erroneously received an error 503 with a message "Over Quota. This application is temporarily over its serving quota. Please try again later." This occurred despite applications being within their quotas. The distribution of these errors was not uniform; some applications received a disproportionately high fraction of the total errors.
## ROOT CAUSE:
A latent bug in the App Engine quota handling code was triggered during a routine software update of the quota system. This resulted in App Engine returning over-quota errors to some applications that were not over quota. As App Engine software updates are rolled out progressively, only some applications were affected by the update before the issue was detected and remediated.
REMEDIATION AND PREVENTION:
Google engineers directed traffic away from the affected App Engine infrastructure once the nature of the problem was understood. This led to the return of global 503 rates to pre-incident levels at 13:53. Google engineers identified a small number of applications that escaped the initial change and fixed their quota behavior manually at 14:45.
In order to prevent recurrence of this issue, Google engineers will add monitoring and alerting for the quota issue that resulted in spurious 503 errors, create a new quick response protocol for handling erroneous quota responses, and will modify application quota behavior to tolerate novel quota system behavior with lower application impact.

# [appengine/15010](https://status.cloud.google.com/incident/appengine/15010)
12:25 Apr 15, 2015
## SUMMARY:
On Friday 10th April 2015, attempts to create or update Datastore indexes failed for some Google App Engine applications for a duration of 148 minutes. In addition, a number of applications retrieved stale data using eventually consistent read operations for an unexpectedly long period. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Friday 10 April 2015 from 11:30 to 13:58 PDT, 331 requests to create or update the definition of Datastore composite indexes across 21 applications failed to complete. In addition, about 34% of applications retrieved stale data using eventually consistent QUERY or GET operations [1]. Unlike strongly consistent queries, it is expected of eventually consistent read operations to return stale data for a brief period. However, this behaviour was extended to a longer duration than that which is typically observed during normal operations. There was no impact on strongly consistent operations.
During the recovery phase of this incident about 7% of Google App Engine applications experienced elevated latency on PUT operations for 15 minutes.
## ROOT CAUSE:
During a planned maintenance activity, undertaken to create a new Datastore replica to accommodate organic growth, incorrectly configured automation created an unnecessary large table in the new replica. This resulted in exhaustion of resources allocated to Datastore and write failures to this replica. Once the underlying problem was resolved, a high volume of writes were routed to the new replica, resulting in elevated latency for write operations.
REMEDIATION AND PREVENTION:
At 00:30 PDT on Friday 10th April 2015, an automated alert on resource depletion was sent out to Google Engineers. However, this alert was suppressed, as is normal practice when undertaking this type of maintenance activity. At 11:30 PDT, quota allocated to the replica was exhausted. Google Engineers were notified by internal teams at 12:53 PDT of problems with Datastore indexes. At 13:26 PDT, Google Engineers deleted the problematic large table and started the procedure to reserve additional quota for this storage replica. This took effect at 13:35 PDT and the replica started receiving write requests immediately, which caused a brief increase in latency. Normal operation was restored at 13:58 PDT.
To prevent similar incidents in future, we are modifying our maintenance procedures to avoid suppression of the appropriate alerts, and to ensure that this large table is created under close monitoring.
[1]. Details on eventual and strong consistency on Google Cloud Datastore: https://cloud.google.com/developers/articles/balancing-strong-and-eventual-consistency-with-google-cloud-datastore/#h.tf76fya5nqk8

# [appengine/15011](https://status.cloud.google.com/incident/appengine/15011)
05:46 Apr 24, 2015
## SUMMARY:
On Friday 17 April 2015, the Google App Engine Logs API experienced intermittent failures and reduced throughput for read requests for a duration of 54 minutes. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Friday 17 April 2015 from 16:02 to 16:56 PDT, 3% of read requests to the Logs API failed and there was a 96% drop in throughput. The problem affected 16% of applications that rely on this API to export logs. In this time window, users experienced intermittent timeouts while attempting to view application logs on App Engine Admin Console or Google Cloud Developers console.
## ROOT CAUSE:
Hotspotting in the App Engine Logs API's storage subsystem caused a number of storage nodes to fail. This eventually resulted in resource depletion and request failures.
REMEDIATION AND PREVENTION:
At 16:05 on Friday 17 April 2015, an automated alert on depletion of available resources for the Logs API was sent out to Google Engineers. To resolve the immediate problem they started redirecting traffic away from the affected storage layer. The service started recovering at 16:51 and normal operation was restored at 16:56.
To prevent similar incidents in future, we are implementing changes to reallocate resources consumed by high use individual nodes of the storage layer backing the Logs API.

# [appengine/15012](https://status.cloud.google.com/incident/appengine/15012)
10:36 Apr 23, 2015
## SUMMARY:
On Wednesday 22 April 2015, for a duration of 92 minutes, some requests from European regions to Google App Engine custom domains were redirected to the Google front page. We apologise to our customers and users who were affected by this issue, and we have taken and are taking immediate steps to improve the platformâs availability.
## DETAILED DESCRIPTION OF IMPACT:
Starting at 06:37 PDT on Wednesday 22 April, some custom-domain URL requests from the Europe region were redirected to the www.google.com front page, or to equivalent national Google front pages, instead of being dispatched to their target Google App Engine applications.
The incident had two phases. In the first phase, from 06:37 to 07:30, 7.9% of traffic to custom domains was affected. In the second phase, from 07:30 to 08:09, 13.7% of custom domain traffic was affected. In total, approximately 0.2% of requests to App Engine were incorrectly redirected during the incident.
Requests originating outside Europe were not affected, except for a very small percentage which were routed to the Google network through European points of presence. Requests to applications via appspot.com domains were also not affected. The hosting region of the application was not a factor.
## ROOT CAUSE:
App Engine custom domains are handled by a system which performs domain mapping for a number of Google services. In order to increase performance, capacity and supportability, Google engineers are in the process of migrating this system's traffic onto Google's general-purpose network infrastructure.
The outage commenced when a rollout of this integration began in European datacenters, with a small fraction of custom domain requests being routed through the general infrastructure. Detailed monitoring was in place for this migration but, incorrectly, did not include App Engine custom domains. Due to a configuration error, the migrated App Engine custom domains were not recognized by the infrastructure, which therefore redirected them to its default target of the Google front page.
REMEDIATION AND PREVENTION:
At 08:04, the issue was identified and Google engineers immediately cancelled the rollout, restoring service by 08:09.
To prevent similar issues from reaching production in future, Google engineers are implementing software release tests to identify the class of configuration error that triggered the incident.
In case similar issues do reach production, Google engineers are extending rollout testing to include App Engine custom domains so that problematic rollouts will be detected and cancelled automatically and immediately.
Finally, continuous monitoring will be added to ensure that all types of custom domain are being correctly recognized and dispatched by the infrastructure, so that Google engineers will be rapidly notified if similar issues recur, regardless of the cause.

# [appengine/15013](https://status.cloud.google.com/incident/appengine/15013)
04:24 Apr 30, 2015
## SUMMARY:
For 4 hours and 37 minutes on Tuesday 28 April 2015, 45% of Google App Engine deployments failed. If you were trying to deploy new versions of your app during this time, we apologize for the extended outage and the delay on public announcement.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 28 April 2015 from 12:05 to 16:42 PDT, 45% of App Engine deployments experienced delays that resulted in the operation timing out. A small number of deployments were exceptionally slow but succeeded. There was no impact to already-deployed applications, nor to applications after a successful deployment.
Affected deployments showed the messages, "Checking if deployment succeeded" and "Will check again in 60 seconds" for long periods. Deployments that timed out showed, "Version still not ready to serve, aborting" and "An unexpected error occurred. Aborting".
## ROOT CAUSE:
Google engineers ran an internal software upgrade that has a side-effect of slowing some deployments for a period of up to one hour. The upgrade failed in its first run and had to be restarted, extending the duration of its impact. Most affected deployments were delayed beyond their timeout period, causing the deployment to be aborted.
REMEDIATION AND PREVENTION:
Google engineers are improving the deployment infrastructure to minimize the impact of routine maintenance. Google will also make app deployment speed and reliability more transparent to customers.
In case of future deployment delays, Google is updating procedures to ensure that public notifications are issued in a timely fashion.

# [appengine/15019](https://status.cloud.google.com/incident/appengine/15019)
19:57 Jun 18, 2015
## SUMMARY:
On Tuesday, 16 June 2015, Google App Engine Task Queue service and App Engine application deployment experienced increased error rates for a duration of 3 hours and 25 minutes. If your service or application was affected, we apologize.  We have taken actions to fix the issue and are in process of making the system more reliable.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday, 16 June 2015 from 20:10 to 23:35 PDT, some developers of Google App Engine applications in the US region were unable to deploy their applications.  The overall error rate of deployments during this period was approximately 60%.  Affected developers saw that attempted deployments would exit and report an internal server error message after HTTP requests to appengine.google.com timed out.  App Engine Admin Console was unable to load data for affected applications.  Additionally, between 20:58 to 21:33, applications in the US region experienced an increase in error rate of up to 0.25% as well as slower execution of Task Queue tasks.
## ROOT CAUSE:
Google engineers had performed maintenance on a storage system of one of datacenters which App Engine uses.  During this maintenance, components of App Engine that rely on this storage system had to rely on a replica in a different datacenter. For both deployments and Task Queues, this switch did not function properly.
REMEDIATION AND PREVENTION:
Google engineers took necessary measures to prevent the Task Queue service from accessing the storage under the maintenance at 21:33.  In addition, all traffic for the affected applications was redirected to alternate datacenters at 23:26.  This was completed by 23:35 and applications were again able to deploy successfully.
To prevent the issue from recurring, we are working to make deployments and Task Queue are more resilient to movements in the underlying storage system, in a similar fashion to other App Engine components.

# [appengine/15020](https://status.cloud.google.com/incident/appengine/15020)
16:30 Aug 13, 2015
## SUMMARY:
On Wednesday, 12 August 2015, the Search API for Google App Engine experienced increased latency and errors for 40 minutes.  We apologize for this incident and the effect it had on applications using the Search API.  We strive for excellent performance and uptime, so we will take appropriate actions right away to improve the Search APIâs availability.
If you believe your paid application experienced an SLA violation as a result of this incident, please contact us at: https://support.google.com/cloud/answer/3420056
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday, 12 August 2015 from 11:05am to 11:45am PDT, the Search API service experienced an increase in latency and error rate.  8.7% of applications using the Search API received a 7.5% error rate with messages like: âTimeout: Failed to complete request in NNNNmsâ
## ROOT CAUSE:
A set of queries sent to a Google-owned service running on App Engine caused the Search API service to fail.
REMEDIATION AND PREVENTION:
At 10:28, Google engineers were automatically alerted to increasing latency in the Search API backend, but at this point, customers were not impacted. At 11:05, the increasing latency started causing Search API timeouts.  Once the cause of the latency increase was discovered, the relevant user was isolated from other customers, ending the incident at 11:45.
The Search API team is implementing mitigation and monitoring changes as a result of this incident, which include changes to the API backend to isolate the impact of similar issues and improved monitoring to reduce the time taken to detect and isolate problematic workloads for the Search API.

# [appengine/15021](https://status.cloud.google.com/incident/appengine/15021)
10:00 Sep 19, 2015
## SUMMARY:
On Thursday 17 September 2015, Google App Engine experienced increased latency and HTTP errors for 1 hour 28 minutes. We apologize to our customers who were affected by this issue.  This is not the level of quality and reliability we strive to offer you, and we are taking immediate steps to prevent similar issues from occurring in future.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 17 September 2015 from 12:40 to 14:08 PDT, <0.01% of applications using Google App Engine experienced elevated latencies, HTTP error rates, and failures for the memcache API. The Google Developers Console was also affected and experienced timeouts during the time.
## ROOT CAUSE:
An unhealthy Managed VMs application triggered an excessive number of retries in the App Engine infrastructure in a single datacenter. App Engine's serving stack automatically detected the overload, and diverted the majority of traffic to an alternate datacenter. Memcache was unavailable for apps which were diverted in this manner; this increased latency for those apps. Latency was also increased by the need to create new instances to run those apps in the alternate datacenter. Traffic which was not diverted experienced errors due to the overload.
REMEDIATION AND PREVENTION:
At 12:47, Google engineers were automatically alerted to increasing latency, followed by elevated error rate, for App Engine, and started investigating the root cause of the issue. The incident was resolved at 14:08.
Google engineers are rolling out a fix which curbs the excessive number of retries that caused this incident. Additionally, the team is implementing improved monitoring to reduce the time taken to detect and isolate problematic workloads.

# [appengine/15023](https://status.cloud.google.com/incident/appengine/15023)
12:22 Nov 13, 2015
## SUMMARY:
On Tuesday, 10 November 2015, outbound traffic going through one of our European routers from both Google Compute Engine and Google App Engine experienced high latency for a duration of 6h43m minutes. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we have taken and are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday, 10 November 2015 from 06:30 - 13:13 PST, a subset of outbound traffic from Google Compute Engine VMs and Google App Engine instances experienced high latency.  The disruption to service was limited to outbound traffic through one of our European routers, and caused at peak 40% of all traffic being routed through this device to be dropped. This accounted for 1% of all Google Compute Engine traffic being routed from EMEA and <0.05% of all traffic for Google App Engine.
## ROOT CAUSE:
A network component failure in one of our European routers temporarily reduced network capacity in the region causing network congestion for traffic traversing this route. Although the issue was mitigated by changing the traffic priority, the problem was only fully resolved when the affected hardware was replaced.
REMEDIATION AND PREVENTION:
As soon as significant traffic congestion in the network path was detected, at 09:10 PST, Google Engineers diverted a subset of traffic away from the affected path. As this only slightly decreased the congestion, Google Engineers made a change in traffic priority which fully mitigated the problem by 13:13 PST time. The replacement of the faulty hardware resolved the problem.
To address time to resolution, Google engineers have added appropriate alerts to the monitoring of this type of router, so that similar congestion events will be spotted significantly more quickly in future. Additionally, Google engineers will ensure that capacity plans properly account for all types of traffic in single device failures. Furthermore, Google engineers will audit and augment capacity in this region to ensure sufficient redundancy is available.

# [appengine/15025](https://status.cloud.google.com/incident/appengine/15025)
07:40 Dec 16, 2015
## SUMMARY:
On Monday 7 December 2015, 1.29% of Google App Engine applications received errors when issuing authenticated calls to Google APIs over a period of 17 hours and 3 minutes. During a 45-minute period, authenticated calls to Google APIs from outside of App Engine also received errors, with the error rate peaking at 12%. We apologise for the impact of this issue on you and your service. We consider service degradation of this level and duration to be very serious and we are planning many changes to prevent this occurring again in the future.
## DETAILED DESCRIPTION OF IMPACT:
Between Monday 7 December 2015 20:09 PST and Tuesday 8 December 2015 13:12, 1.29% of Google App Engine applications using service accounts received error 401 "Access Denied" for all requests to Google APIs requiring authentication. Unauthenticated API calls were not affected. Different applications experienced impact at different times, with few applications being affected for the full duration of the incident.
In addition, between 23:05 and 23:50, an average of 7% of all requests to Google Cloud APIs failed or timed out, peaking briefly at 12%. Outside of this time only API calls from App Engine were affected.
## ROOT CAUSE:
Google engineers have recently carried out a migration of the Google Accounts system to a new storage backend, which included copying API authentication service credentials data and redirecting API calls to the new backend.
To complete this migration, credentials were scheduled to be deleted from the previous storage backend. This process started at 20:09 PST on Monday 7 December 2015. Due to a software bug, the API authentication service continued to look up some credentials, including those used by Google App Engine service accounts, in the old storage backend. As these credentials were progressively deleted, their corresponding service accounts could no longer be authenticated.
The impact increased as more credentials were deleted and some Google App Engine applications started to issue a high volume of retry requests.  At 23:05, the retry volume exceeded the regional capacity of the API authentication service, causing 1.3% of all authenticated API calls to fail or timeout, including Google APIs called from outside Google App Engine. At 23:30 the API authentication service exceeded its global capacity, causing up to 12% of all authenticated API calls to fail until 23:50, when the overload issue was resolved.
REMEDIATION AND PREVENTION:
At 23:50 PST on Monday 8 December, Google engineers blocked certain authentication credentials that were known to be failing, preventing retries on these credentials from overloading the API authentication service.
On Tuesday 9 December 08:52 PST, the deletion process was halted, having removed 2.3% of credentials, preventing further applications from being affected. At 10:08, Google engineers identified the root cause for the misdirected credentials lookup. After thorough testing, a fix was rolled out globally, resolving the issue for all affected Google App Engine applications by 13:12.
Google has conducted a far-reaching review of the issue's root causes and contributory factors, leading to numerous prevention and mitigation actions in the following areas:
â Google engineers have deployed monitoring for additional infrastructure signals to detect and analyse similar issues more quickly.
â Google engineers have improved internal tools to extend auditing and logging and automatically advise relevant teams on potentially risky data operations.
â Additional rate limiting and caching features will be added to the API authentication service, increasing its resilience to load spikes.
â Googleâs development guidelines are being reviewed and updated to improve the handling of service or backend migrations, including a grace period of disabling access to old data locations before fully decommissioning them.
Our customers rely on us to provide a superior service and we regret we did not live up to expectations in this case. We apologize again for the inconvenience this caused you and your users.

# [appengine/16002](https://status.cloud.google.com/incident/appengine/16002)
19:05 Feb 04, 2016
## SUMMARY:
On Wednesday 3 February 2016, some App Engine applications running on Java7, Go and Python runtimes served errors with HTTP response 500 for a duration of 18 minutes.  We sincerely apologize to customers who were affected.  We have taken and are taking immediate steps to improve the platform's performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 3 February 2016, from 18:37 PST to 18:55 PST, 1.1% of Java7, 3.1% of Go and 0.2% of all Python applications served errors with HTTP response code 500.  The impact varied across applications, with less than 0.8% of all applications serving more than 100 errors during this time period.  The distribution of errors was heavily tail-weighted, with a few applications receiving a large fraction of errors for their traffic during the event.
## ROOT CAUSE:
An experiment meant to test a new feature on a small number of applications was inadvertently applied to Java7 and Go applications globally.  Requests to these applications tripped over the incompatible experimental feature, causing the instances to shut down without serving any requests successfully, while the depletion of healthy instances caused these applications to serve HTTP requests with a 500 response.  Additionally, the high rate of failure in Java and Go instances caused resource contention as the system tried to start new instances, which resulted in collateral damage to a small number of Python applications.
REMEDIATION AND PREVENTION:
At 18:35, a configuration change was erroneously enabled globally instead of to the intended subset of applications.  Within a few minutes, Google Engineers noticed a drop in global traffic to GAE applications and determined that the configuration change was the root cause.  At 18:53 the configuration change was rolled back and normal operations were restored by 18:55.
To prevent a recurrence of this problem, Google Engineers are modifying the fractional push framework to inhibit changes which would simultaneously apply to the majority of applications, and creating telemetry to accurately predict the fraction of instances affected by a given change.  Google Engineers are also enhancing the alerts on traffic drop and error spikes to quickly identify and mitigate similar incidents.

# [appengine/16003](https://status.cloud.google.com/incident/appengine/16003)
22:57 Apr 25, 2016
## SUMMARY:
On Tuesday 19th April 2016, 1.1% of all requests to obtain new Google OAuth 2.0 tokens failed for a period of 70 minutes. Users of affected applications experienced authentication errors. This incident affected all Google services that use OAuth.
We apologize to any customer whose application was impacted by this incident. We take outages very seriously and are strongly focused on learning from these incidents to improve the future reliability of our services.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 19 April 2016 from 06:12 to 07:22 PDT, the Google OAuth 2.0 service returned HTTP 500 errors for 1.1% of all requests.
OAuth tokens are granted to applications on behalf of users. The application requesting the token is identified by its client ID. Google's OAuth service looks up the application associated with a client ID before granting the new token. If the mapping from client ID to application is not cached by Google's OAuth service, then it is fetched from a separate client ID lookup service. The client ID lookup service dropped some requests during the incident, which caused those token requests to fail.
The token request failures predominantly affected applications which had not populated the client ID cache because they were less frequently used. Such infrequently-used applications may have experienced high error rates on token requests for their users, though the overall average error rate was 1.1% measured across all applications.
Once access tokens were obtained, they could be used without problems. Tokens issued before the incident continued to function until they expired.
Any requests for tokens that did not use a client ID were not affected by this incident.
## ROOT CAUSE:
Google's OAuth system depends on an internal service to lookup details of the client ID that is making the token request.
During this incident, the client ID lookup service had insufficient capacity to respond to all requests to lookup client ID details.
Before the incident started, the client ID lookup service had been running close to its rated capacity. In an attempt to prevent a future problem, Google SREs triggered an update to add capacity to the service at 05:30.
Normally adding capacity does not cause a restart of the service. However, the update process had a misconfiguration which caused a rolling restart. While servers were restarting, the capacity of the service was reduced further.
In addition, the restart triggered a bug in a specific client's code that caused its cache to be invalidated, leading to a spike in requests from that client.
Google's systems are designed to throttle clients in these situations. However, the throttling was insufficient to prevent overloading of the client ID lookup service. Google's software load balancer was configured to drop a fraction of incoming requests to the client ID lookup service during overload in order to prevent cascading failure. In this case, the load balancer was configured too conservatively and dropped more traffic than needed.
REMEDIATION AND PREVENTION:
Google's internal monitoring systems detected the incident at 06:28 and our engineers isolated the root cause as an overload in the client ID lookup service at 06:47. We added additional capacity to work around the issue at 07:07 and the error rate dropped to normal levels by 07:22.
In order to prevent future incidents of this type from occurring, we are taking several actions.

We will improve our monitoring to detect immediately when usage of the client ID lookup service gets close to its capacity.
We will ensure that the client ID lookup service always has more than 10% spare capacity at peak.
We will change the load balancer configuration so that it will not uniformly drop traffic when overloaded. Instead, the load balancer will throttle the clients that are causing traffic spikes.
We will change the update process to minimize the capacity that is temporarily lost during an update.
We will fix the client bug that caused its client ID cache to be invalidated.


# [appengine/16008](https://status.cloud.google.com/incident/appengine/16008)
09:54 Aug 23, 2016
## SUMMARY:
On Thursday 11 August 2016, 21% of Google App Engine applications hosted in the US-CENTRAL region experienced error rates in excess of 10% and elevated latency between 13:13 and 15:00 PDT.  An additional 16% of applications hosted on the same GAE instance observed lower rates of errors and latency during the same period.
We apologize for this incident. We know that you choose to run your applications on Google App Engine to obtain flexible, reliable, high-performance service, and in this incident we have not delivered the level of reliability for which we strive. Our engineers have been working hard to analyze what went wrong and ensure incidents of this type will not recur.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 11 August 2016 from 13:13 to 15:00 PDT, 18% of applications hosted in the US-CENTRAL region experienced error rates between 10% and 50%, and 3% of applications experienced error rates in excess of 50%.  Additionally, 14% experienced error rates between 1% and 10%, and 2% experienced error rate below 1% but above baseline levels.  In addition, the 37% of applications which experienced elevated error rates also observed a median latency increase of just under 0.8 seconds per request.
The remaining 63% of applications hosted on the same GAE instance, and applications hosted on other GAE instances, did not observe elevated error rates or increased latency.
Both App Engine Standard and Flexible Environment applications in US-CENTRAL were affected by this incident. In addition, some Flexible Environment applications were unable to deploy new versions during this incident.
App Engine applications in US-EAST1 and EUROPE-WEST were not impacted by this incident.
## ROOT CAUSE:
The incident was triggered by a periodic maintenance procedure in which Google engineers move App Engine applications between datacenters in US-CENTRAL in order to balance traffic more evenly.
As part of this procedure, we first move a proportion of apps to a new datacenter in which capacity has already been provisioned. We then gracefully drain traffic from an equivalent proportion of servers in the downsized datacenter in order to reclaim resources. The applications running on the drained servers are automatically rescheduled onto different servers.
During this procedure, a software update on the traffic routers was also in progress, and this update triggered a rolling restart of the traffic routers.  This temporarily diminished the available router capacity.
The server drain resulted in rescheduling of multiple instances of manually-scaled applications. App Engine creates new instances of manually-scaled applications by sending a startup request via the traffic routers to the server hosting the new instance.
Some manually-scaled instances started up slowly, resulting in the App Engine system retrying the start requests multiple times which caused a spike in CPU load on the traffic routers. The overloaded traffic routers dropped some incoming requests.
Although there was sufficient capacity in the system to handle the load, the traffic routers did not immediately recover due to retry behavior which amplified the volume of requests.
REMEDIATION AND PREVENTION:
Google engineers were monitoring the system during the datacenter changes and immediately noticed the problem. Although we rolled back the change that drained the servers within 11 minutes, this did not sufficiently mitigate the issue because retry requests had generated enough additional traffic to keep the systemâs total load at a substantially higher-than-normal level.
As designed, App Engine automatically redirected requests to other datacenters away from the overload - which reduced the error rate. Additionally, our engineers manually redirected all traffic at 13:56 to other datacenters which further mitigated the issue.
Finally, we then identified a configuration error that caused an imbalance of traffic in the new datacenters. Fixing this at 15:00 finally fully resolved the incident.
In order to prevent a recurrence of this type of incident, we have added more traffic routing capacity in order to create more capacity buffer  when draining servers in this region.
We will also change how applications are rescheduled so that the traffic routers are not called and also modify that the system's retry behavior so that it cannot trigger this type of failure.
We know that you rely on our infrastructure to run your important workloads and that this incident does not meet our bar for reliability. For that we apologize. Your trust is important to us and we will continue to all we can to earn and keep that trust.

# [appengine/16009](https://status.cloud.google.com/incident/appengine/16009)
18:17 Aug 30, 2016
## SUMMARY:
On Monday 22 August 2016, the Google Cloud US-CENTRAL1-F zone lost network connectivity to services outside that zone for a duration of 25 minutes. All other zones in the US-CENTRAL1 region were unaffected. All network traffic within the zone was also unaffected.
We apologize to customers whose service or application was affected by this incident. We understand that a network disruption has a negative impact on your application - particularly if it is homed in a single zone - and we apologize for the inconvenience this caused. What follows is our detailed analysis of the root cause and actions we will take in order to prevent this type of incident from recurring.
## DETAILED DESCRIPTION OF IMPACT:
We have received feedback from customers asking us to specifically and separately enumerate the impact of incidents to any service that may have been touched. We agree that this will make it easier to reason about the impact of any particular event and we have done so in the following descriptions.
On Monday 22 August 2016 from 07:05 to 07:30 PDT the Google Cloud US-CENTRAL1-F zone lost network connectivity to services outside that zone.
App Engine
6% of App Engine Standard Environment applications in the US-CENTRAL region served elevated error rates for up to 8 minutes, until the App Engine serving infrastructure automatically redirected traffic to a failover zone. The aggregate error rate across all impacted applications during the incident period was 3%. The traffic redirection caused a Memcache flush for affected applications, and also loading requests as new instances of the applications started up in the failover zones.
All App Engine Flexible Environment applications deployed to the US-CENTRAL1-F zone were unavailable for the duration of the incident. Additionally, 4.5% of these applications experienced various levels of unavailability for up to an additional 5 hours while the system recovered.
Deployments for US-CENTRAL Flexible applications were delayed during the incident. Our engineers disabled the US-CENTRAL1-F zone for new deployments during the incident, so that any customers who elected to redeploy, immediately recovered.
Cloud Console
The Cloud Console was available during the incident, though some App Engine administrative pages did not load for applications in US-CENTRAL and 50% of project creation requests failed to complete and needed to be retried by customers before succeeding.
Cloud Dataflow
Some Dataflow running jobs in the US-CENTRAL1 region experienced delays in processing. Although most of the affected jobs recovered gracefully after the incident ended, up to 2.5% of affected jobs in this zone became stuck and required manual termination by customers. New jobs created during the incident were not impacted.
Cloud SQL
Cloud SQL First Generation instances were not impacted by this incident.
30% of Cloud SQL Second Generation instances in US-CENTRAL1 were unavailable for up to 5 minutes, after which they became available again. An additional 15% of Second Generation instances were unavailable for 22 minutes.
Compute Engine
All instances in the US-CENTRAL1-F zone were inaccessible from outside the zone for the duration of the incident. 9% of them remained inaccessible from outside the zone for an additional hour.
Container Engine
Container Engine clusters running in US-CENTRAL1-F were inaccessible from outside of the zone during the incident although they continued to serve.
In addition, calls to the Container Engine API experienced a 4% error rate and elevated latency during the incident, though this was substantially mitigated if the client retried the request.
Stackdriver Logging
20% of log API requests sent to Stackdriver Logging in the US-CENTRAL1 region failed during the incident, though App Engine logging was not impacted. Clients retrying requests recovered gracefully.
Stackdriver Monitoring
Requests to the StackDriver web interface and the Google Monitoring API v2beta2 and v3 experienced elevated latency and an error rate of up to 3.5% during the incident. In addition, some alerts were delayed. Impact for API calls was substantially mitigated if the client retried the request.
## ROOT CAUSE:
On 18 July, Google carried out a planned maintenance event to inspect and test the UPS on a power feed in one zone in the US-CENTRAL1 region. That maintenance disrupted one of the two power feeds to network devices that control routes into and out of the US-CENTRAL1-F zone.
Although this did not cause any disruption in service, these devices unexpectedly and silently disabled the affected power supply modules - a previously unseen behavior. Because our monitoring systems did not notify our network engineers of this problem the power supply modules were not re-enabled after the maintenance event.
The service disruption was triggered on Monday 22 August, when our engineers carried out another planned maintenance event that removed power to the second power feed of these devices, causing them to disable the other power supply module as well, and thus completely shut down.
Following our standard procedure when carrying out maintenance events, we made a detailed line walk of all critical equipment prior to, and after, making any changes. However, in this case we did not detect the disabled power supply modules.
Loss of these network devices meant that machines in US-CENTRAL1-F did not have routes into and out of the zone but could still communicate to other machines within the same zone.
REMEDIATION AND PREVENTION:
Our network engineers received an alert at 07:14, nine minutes after the incident started. We restored power to the devices at 07:30. The network returned to service without further intervention after power was restored.
As immediate followup to this incident, we have already carried out an audit of all other network devices of this type in our fleet to verify that there are none with disabled power supply modules.
We have also written up a detailed post mortem of this incident and will take the following actions to prevent future outages of this type:
Our monitoring will be enhanced to detect cases in which power supply modules are disabled. This will ensure that conditions that are missed by the manual line walk prior to maintenance events are picked up by automated monitoring.
We will change the configuration of these network devices so that power disruptions do not cause them to disable their power supply modules.
The interaction between the network control plane and the data plane should be such that the data plane should "fail open" and continue to route packets in the event of control plane failures.  We will add support for networking protocols that have the capability to continue to route traffic for a short period in the event of failures in control plane components.
We will also be taking various actions to improve the resilience of the affected  services to single-zone outages, including the following:
App Engine
Although App Engine Flexible Environment is currently in Beta, we expect production services to be more resilient to single zone disruptions. We will make this extra resilience an exit criteria before we allow the service to reach General Availability.
Cloud Dataflow
We will improve resilience of Dataflow to single-zone outages by implementing better strategies for migrating the job controller to a new zone in the event of an outage. Work on this remediation is already underway.
Stackdriver Logging
We will make improvements to the Stackdriver Logging service (currently in Beta) in the areas of automatic failover and capacity management before this service goes to General Availability. This will ensure that it is resilient to single-zone outages.
Stackdriver Monitoring
The Google Monitoring API (currently in beta) is already hosted in more than one zone, but we will further improve its resilience by adding additional capacity to ensure a single-zone outage does not cause overload in any other zones. We will do this before this service exits to General Availability.
Finally, we know that you depend on Google Cloud Platform for your production workloads and we apologize for the inconvenience this event caused.

# [appengine/17005](https://status.cloud.google.com/incident/appengine/17005)
10:07 Jun 13, 2017
## ISSUE SUMMARY:
On Wednesday 7 June 2017, Google App Engine experienced highly elevated serving latency and timeouts for a duration of 138 minutes. If your service or application was affected the increase in latency, we sincerely apologize â this is not the level of reliability and performance we expect of our platform, and we are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 7 June 2017, from 13:34 PDT to 15:52 PDT, 7.7% of active applications on the Google App Engine service experienced severely elevated latency; requests that typically take under 500ms to serve were taking many minutes. This elevated latency would have either resulted in users seeing additional latency when waiting for responses from the affected applications or 500 errors if the application handlers timed out.  The individual application logs would have shown this increased latency or increases in âRequest was aborted after waiting too long to attempt to service your requestâ error messages.
## ROOT CAUSE:
The incident was triggered by an increase in memory usage across all App Engine appservers in a datacenter in us-central.  An App Engine appserver is responsible for creating instances to service requests for App Engine applications. When its memory usage increases to unsustainable levels, it will stop some of its current instances, so that they can be rescheduled on other appservers in order to balance out the memory requirements across the datacenter.  This transfer of an App Engine instance between appservers consumes CPU resources, a signal used by the master scheduler of the datacenter to detect when it must further rebalance traffic across more appservers (such as when traffic to the datacenter increases and more App Engine instances are required).
Normally, these memory management techniques are transparent to customers but in isolated cases, they can be exacerbated by large amounts of additional traffic being routed to the datacenter, which requires more instances to service user requests.  The increased load and memory requirement from scheduling new instances combined with rescheduling instances from appservers with high memory usage resulted in most appservers being considered âbusyâ by the master scheduler.  User requests needed to wait for an available instance to either be transferred or created before they were able to be serviced, which results in the increased latency seen at the app level.
REMEDIATION AND PREVENTION
Latencies began to increase at 13:34 PDT and Google engineers were alerted to the increase in latency at 13:45 PDT and were able to identify a subset of traffic that was causing the increase in memory usage.  At 14:08, they were able to limit this subset of traffic to an isolated partition of the datacenter to ease the memory pressure on the remaining appservers.  Latency for new requests started to improve as soon as this traffic was isolated; however, tail latency was still elevated due to the large backlog of requests that had accumulated since the incident started.  This backlog was eventually cleared by 15:52 PDT.  To prevent further recurrence, traffic to the affected datacenter was rebalanced with another datacenter.
To prevent future recurrence of this issue, Google engineers will be re-evaluating the resource distribution in the us-central datacenters where App Engine instances are hosted.  Additionally, engineers will be developing stronger alerting thresholds based on memory pressure signals so that traffic can be redirected before latency increases.  And finally, engineers will be evaluating changes to the scheduling strategy used by the master scheduler responsible for scheduling appserver work to prevent this situation in the future.

# [appengine/17006](https://status.cloud.google.com/incident/appengine/17006)
07:17 Jun 17, 2017
## ISSUE SUMMARY:
On Thursday 8 June 2017, from 08:24 to 09:26 US/Pacific Time, datacenters in the asia-northeast1 region experienced a loss of network connectivity for a total of 62 minutes. We apologize for the impact this issue had on our customers, and especially to those customers with deployments across multiple zones in the asia-northeast1 region. We recognize we failed to deliver the regional reliability that multiple zones are meant to achieve.
We recognize the severity of this incident and have completed an extensive internal postmortem.  We thoroughly understand the root causes and no datacenters are at risk of recurrence.  We are at work to add mechanisms to prevent and mitigate this class of problem in the future.  We have prioritized this work and in the coming weeks, our engineering team will complete the action items we have generated from the postmortem.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 8 June 2017, from 08:24 to 09:26 US/Pacific Time, network connectivity to and from Google Cloud services running in the asia-northeast1 region was unavailable for 62 minutes.  This issue affected all Google Cloud Platform services in that region, including Compute Engine, App Engine, Cloud SQL, Cloud Datastore, and Cloud Storage.  All external connectivity to the region was affected during this time frame, while internal connectivity within the region was not affected.
In addition, inbound requests from external customers originating near Googleâs Tokyo point of presence intended for Compute or Container Engine HTTP Load Balancing were lost for the initial 12 minutes of the outage. Separately, Internal Load Balancing within asia-northeast1 remained degraded until 10:23.
## ROOT CAUSE:
At the time of incident, Google engineers were upgrading the network topology and capacity of the region; a configuration error caused the existing links to be decommissioned before the replacement links could provide connectivity, resulting in a loss of connectivity for the asia-northeast1 region. Although the replacement links were already commissioned and appeared to be ready to serve, a network-routing protocol misconfiguration meant that the routes through those links were not able to carry traffic.
As Google's global network grows continuously, we make upgrades and updates reliably by using automation for each step and, where possible, applying changes to only one zone at any time.  The topology in asia-northeast1 was the last region unsupported by automation; manual work was required to be performed to align its topology with the rest of our regional deployments (which would, in turn, allow automation to function properly in the future). This manual change mistakenly did not follow the same per-zone restrictions as required by standard policy or automation, which meant the entire region was affected simultaneously.
In addition, some customers with deployments across multiple regions that included asia-northeast1 experienced problems with HTTP Load Balancing due to a failure to detect that the backends were unhealthy. When a network partition occurs, HTTP Load Balancing normally detects this automatically within a few seconds and routes traffic to backends in other regions. In this instance, due to a performance feature being tested in this region at the time, the mechanism that usually detects network partitions did not trigger, and continued to attempt to assign traffic until our on-call engineers responded.  Lastly, the Internal Load Balancing outage was exacerbated due to a software defined networking component which was stuck in a state where it was not able to provide network resolution for instances in the load balancing group.
REMEDIATION AND PREVENTION
Google engineers were paged by automated monitoring within one minute of the start of the outage, at 08:24 PDT. They began troubleshooting and declared an emergency incident 8 minutes later at 08:32. The issue was resolved when engineers reconnected the network path and reverted the configuration back to the last known working state at 09:22. Our monitoring systems worked as expected and alerted us to the outage promptly.
The time-to-resolution for this incident was extended by the time taken to perform the rollback of the network change, as the rollback had to be performed manually.  We are implementing a policy change that any manual work on live networks be constrained to a single zone. This policy will be enforced automatically by our change management software when changes are planned and scheduled.  In addition, we are building automation to make these types of changes in future, and to ensure the system can be safely rolled back to a previous known-good configuration at any time during the procedure.
The fix for the HTTP Load Balancing performance feature that caused it to incorrectly believe zones within asia-northeast1 were healthy will be rolled out shortly.
SUPPORT COMMUNICATIONS
During the incident, customers who had originally contacted Google Cloud Support in Japanese did not receive periodic updates from Google as the event unfolded. This was due to a software defect in the support tooling â unrelated to the incident described earlier.
We have already fixed the software defect, so all customers who contact support will receive incident updates.  We apologize for the communications gap to our Japanese-language customers.
RELIABILITY SUMMARY
One of our biggest pushes in GCP reliability at Google is a focus on careful isolation of zones from each other.  As we encourage users to build reliable services using multiple zones, we also treat zones separately in our production practices, and we enforce this isolation with software and policy.  Since we missed this markâand affecting all zones in a region is an especially serious outageâwe apologize.  We intend for this incident report to accurately summarize the detailed internal post-mortem that includes final assessment of impact, root cause, and steps we are taking to prevent an outage of this form occurring again.  We hope that this incident report demonstrates the work we do to learn from our mistakes to deliver on this commitment. We will do better.
Sincerely,
Benjamin Lutch | VP Site Reliability Engineering | Google

# [appengine/17007](https://status.cloud.google.com/incident/appengine/17007)
10:59 Nov 07, 2017
## ISSUE SUMMARY:
On Monday 6 November 2017, the App Engine Memcache service experienced unavailability for applications in all regions for 1 hour and 50 minutes.
We sincerely apologize for the impact of this incident on your application or service. We recognize the severity of this incident and will be undertaking a detailed review to fully understand the ways in which we must change our systems to prevent a recurrence.
## DETAILED DESCRIPTION OF IMPACT:
On Monday 6 November 2017 from 12:33 to 14:23 PST, the App Engine Memcache service experienced unavailability for applications in all regions.
Some customers experienced elevated Datastore latency and errors while Memcache was unavailable. At this time, we believe that all the Datastore issues were caused by surges of Datastore activity due to Memcache being unavailable. When Memcache failed, if an application sent a surge of Datastore operations to specific entities or key ranges, then Datastore may have experienced contention or hotspotting, as described in https://cloud.google.com/datastore/docs/best-practices#designing_for_scale. Datastore experienced elevated load on its servers when the outage ended due to a surge in traffic. Some applications in the US experienced elevated latency on gets between 14:23 and 14:31, and elevated latency on puts between 14:23 and 15:04.
Customers running Managed VMs experienced failures of all HTTP requests and App Engine API calls during this incident. Customers using App Engine Flexible Environment, which is the successor to Managed VMs, were not impacted.
## ROOT CAUSE:
The App Engine Memcache service requires a globally consistent view of the current serving datacenter for each application in order to guarantee strong consistency when traffic fails over to alternate datacenters. The configuration which maps applications to datacenters is stored in a global database.
The incident occurred when the specific database entity that holds the configuration became unavailable for both reads and writes following a configuration update. App Engine Memcache is designed in such a way that the configuration is considered invalid if it cannot be refreshed within 20 seconds. When the configuration could not be fetched by clients, Memcache became unavailable.
REMEDIATION AND PREVENTION
Google received an automated alert at 12:34. Following normal practices, our engineers immediately looked for recent changes that may have triggered the incident. At 12:59, we attempted to revert the latest change to the configuration file. This configuration rollback required an update to the configuration in the global database, which also failed. At 14:21, engineers were able to update the configuration by sending an update request with a sufficiently long deadline. This caused all replicas of the database to synchronize and allowed clients to read the mapping configuration.
As a temporary mitigation, we have reduced the number of readers of the global configuration, which avoids the contention during write and led to the unavailability during the incident. Engineering projects are already under way to regionalize this configuration and thereby limit the blast radius of similar failure patterns in the future.

# [appengine/19001](https://status.cloud.google.com/incident/appengine/19001)
17:25 Jan 07, 2019
## ISSUE SUMMARY:
On Wednesday 2 January, 2019, application creation in Google App Engine (App Engine), first-time deployment of Google Cloud Functions (Cloud Functions) per region, and project creation & API management in Cloud Console experienced elevated error rates ranging from 71% to 100% for a duration of 3 hours, 40 minutes starting at 14:40 PST. Workloads already running on App Engine and Cloud Functions, including deployment of new versions of applications and functions, as well as ongoing use of existing projects and activated APIs, were not impacted.
We know that many customers depend on the ability to create new Cloud projects, applications & functions, and apologize for our failure to provide this to you during this time. The root cause of the incident is fully understood and engineering efforts are underway to ensure the issue is not at risk of recurrence.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 2 January, 2019 from 14:40 PST to 18:20 PST, application creation in App Engine, first-time deployments of Cloud Functions, and project creation & API auto-enablement in Cloud Console experienced elevated error rates in all regions due to a recently deployed configuration update to the underlying control plane for all impacted services.
First-time deployments of new Cloud Functions failed. Redeploying existing deployments of Cloud Functions were not impacted. Workloads on already deployed Cloud Functions were not impacted.
App Engine app creation experienced an error rate of 98%. Workloads for deployed App Engine applications were not impacted.
Cloud API enable requests experienced a 97% average error rate while disable requests had a 71% average error rate. Affected users observed these errors when attempting to enable an API via the Cloud Console and API Console.
## ROOT CAUSE:
The control plane responsible for managing new app creations in App Engine, new function deployments in Cloud Functions, project creation & API management in Cloud Console utilizes a metadata store. This metadata store is responsible for persisting and processing new project creations, function deployments, App Engine applications, and API enablements.
Google engineers began rolling out a new feature designed to improve the fault-tolerance of the metadata store. The rollout had been successful in test environments, but triggered an issue in production due to an unexpected difference in configuration, which triggered a bug. The bug caused writes to the metadata store to fail.
REMEDIATION AND PREVENTION
Google engineers were automatically alerted of the elevated error rate within 3 minutes of the incident start and immediately began their investigation.
At 15:17, an issue with our metadata store was identified as the root cause, and mitigation work began. An initial mitigation was applied, but automation intentionally slowed the rollout of this mitigation to minimize risks to production. To reduce time to resolution, Google engineers developed and implemented a new mitigation. The metadata store became fully available at 18:20.
To prevent a recurrence, we will implement additional validation to the metadata storeâs schemas and ensure that test validation of metadata store configuration matches production.
To improve time to resolution for such issues, we are increasing the robustness of our emergency rollback procedures for the metadata store, and creating engineering runbooks for such scenarios.

# [appengine/19007](https://status.cloud.google.com/incident/appengine/19007)
11:11 Mar 14, 2019
## ISSUE SUMMARY:
On Tuesday 12 March 2019, Google's internal blob storage service experienced a service disruption for a duration of 4 hours and 10 minutes. We apologize to customers whose service or application was impacted by this incident. We know that our customers depend on Google Cloud Platform services and we are taking immediate steps to improve our availability and prevent outages of this type from recurring.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 12 March 2019 from 18:40 to 22:50 PDT, Google's internal blob (large data object) storage service experienced elevated error rates, averaging 20% error rates with a short peak of 31% errors during the incident. User-visible Google services including Gmail, Photos, and Google Drive, which make use of the blob storage service also saw elevated error rates, although (as was the case with GCS) the user impact was greatly reduced by caching and redundancy built into those services. There will be a separate incident report for non-GCP services affected by this incident.
The Google Cloud Platform services that experienced the most significant customer impact were the following:
Google Cloud Storage experienced elevated long tail latency and an average error rate of 4.8%. All bucket locations and storage classes were impacted. GCP services that depend on Cloud Storage were also impacted.
Stackdriver Monitoring experienced up to 5% errors retrieving historical time series data. Recent time series data was available. Alerting was not impacted.
App Engine's Blobstore API experienced elevated latency and an error rate that peaked at 21% for fetching blob data. App Engine deployments experienced elevated errors that peaked at 90%. Serving of static files from App Engine also experienced elevated errors.
## ROOT CAUSE:
On Monday 11 March 2019, Google SREs were alerted to a significant increase in storage resources for metadata used by the internal blob service. On Tuesday 12 March, to reduce resource usage, SREs made a configuration change which had a side effect of overloading a key part of the system for looking up the location of blob data. The increased load eventually lead to a cascading failure.
REMEDIATION AND PREVENTION
SREs were alerted to the service disruption at 18:56 PDT and immediately stopped the job that was making configuration changes. In order to recover from the cascading failure, SREs manually reduced traffic levels to the blob service to allow tasks to start up without crashing due to high load.
In order to prevent service disruptions of this type, we will be improving the isolation between regions of the storage service so that failures are less likely to have global impact. We will be improving our ability to more quickly provision resources in order to recover from a cascading failure triggered by high load. We will make software measures to prevent any configuration changes that cause overloading of key parts of the system. We will improve load shedding behavior of the metadata storage system so that it degrades gracefully under overload.

# [bigquery/18003](https://status.cloud.google.com/incident/bigquery/18003)
11:07 Oct 24, 2014
## SUMMARY:
On Monday 13 October 2014, some user-submitted BigQuery jobs experienced increased execution time for a period 13 hours and 18 minutes.  If your jobs were affected by this delayed execution, we apologize; we strive to maintain the highest standard of performance and reliability and failed to uphold that standard in this instance.  We have implemented changes to both address this issue and monitor and prevent future recurrences of this issue.
## DETAILED DESCRIPTION OF IMPACT:
From 00:37 to 13:55 PDT on Monday 13 October 2014, 1.6% of queries experienced scheduling delays of up to four hours and experienced performance degradation during execution.  Affected jobs started to recover by 07:17 and were fully recovered by 13:55.
## ROOT CAUSE:
The BigQuery service received a combination of user queries that led to lock contention in the underlying component responsible for processing large joins and groupings.  This lock contention slowed down both scheduling and query execution.
REMEDIATION AND PREVENTION:
Monitoring systems alerted Google engineers to increased query latency at 02:27.  To address the performance of the service, Google engineers restarted several of the service components, and focused on identifying specific affected queries and projects.  At 07:27, the engineers redirected traffic to an unaffected datacenter to mitigate the effect on new incoming queries.
To prevent further recurrence of this issue, Google engineers have addressed the sources of lock contention responsible for performance degradation, and have added further
instrumentation to help on-call engineers quickly identify problematic combinations of user queries.  Finally, Google engineers have added more stringent detection and alerting in cases of latency increases.

# [bigquery/18004](https://status.cloud.google.com/incident/bigquery/18004)
18:16 Oct 20, 2014
## SUMMARY:
On Wednesday 15 October 2014, 20% of queries to the Google BigQuery streaming API service failed with an internal error over a period of 147 minutes.  If your application was affected by the unavailability of the streaming API, we sincerely apologize; our goal is to set a high standard of availability and reliability, which we failed to meet in this case.  We have taken and are taking immediate action to prevent future recurrences of this issue.
## DETAILED DESCRIPTION OF IMPACT:
From 05:52 to 08:19 PDT on Wednesday 15 October 2014, some users experienced an increase in error rates when querying recently ingested streaming data.  42% of queries executed by 18% of projects during this time were affected by this issue.  Impacted users saw API responses indicating a retriable internal error had occurred.
## ROOT CAUSE:
As part of a standard deployment, Google engineers released new configuration directives between a subset of the systems responsible for ingesting streaming data, and those responsible for serving recently streamed data. However, some components were relying on stale cached configuration data, and when that cached configuration data was refreshed on a subset of systems, queries against tables that contained recently streamed data failed with an internal error.
REMEDIATION AND PREVENTION:
Google engineers received reports from customers regarding errors with the streaming API service at 07:20 and began to direct traffic to alternate data centers that were not affected by this configuration change at 08:14. Error rates began recovering after the redirection of traffic, and the service recovered fully by 08:19.
To prevent further recurrences of this issue, Google engineers are adding more thorough testing and monitoring to the configuration deployment process to detect and prevent stale configuration data from being introduced.  Google engineers are also adding more stringent monitoring and alerting to detect and address elevated error rates sooner.

# [bigquery/18007](https://status.cloud.google.com/incident/bigquery/18007)
22:45 Feb 19, 2015
## SUMMARY:
Between Tuesday 17 February and Wednesday 18 February 2015, load and export jobs to the BigQuery service experienced significant increases in latency for a period of 29 hours.  If your application was affected by this increase in latency, we apologize.  This is not the standard of service BigQuery strives to uphold and we are taking immediate action to prevent these types of disruptions in the future.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 17 February 2015 at 14:46 PST, all submitted load jobs began to experience elevated latency, ranging from minutes to hours of additional processing latency at the 99th percentile during the incident. The impact varied for each project and was dependent on the size of their respective load jobs.  All incoming load jobs were affected until 18 February 2015 at 19:45 PST.
## ROOT CAUSE:
The BigQuery service received an elevated number of high volume load jobs which overwhelmed the existing ingestion capacity and caused newly created jobs to wait increasingly longer to be scheduled.
REMEDIATION AND PREVENTION:
In response to the increased latency, Google engineers provisioned more resources for load jobs at 12:11 PST on 18 February 2015, providing a short term improvement in processing latency.  The BigQuery engineering team then isolated the subset of jobs which were overwhelming system capacity.  Google Support engineers were able to confirm with the job owners that the jobs were unnecessary and safe to terminate, which the BigQuery engineering team proceeded to do, allowing processing latency to return to normal.
Google engineers are working on the resource allocation system for large scale import jobs to limit the possibility of a concentrated number of intensive load jobs overwhelming system resources.  They will also be optimizing monitoring and alerting for increased latency and active jobs waiting to be executed.  Finally, they will be exploring new ways of exposing job management to customers.

# [bigquery/18008](https://status.cloud.google.com/incident/bigquery/18008)
21:08 May 08, 2015
## SUMMARY:
On Thursday 7 May 2015, requests to the Google BigQuery Web UI and APIs experienced errors for a total duration of 2 hours and 9 minutes over two separate periods.  We understand the high level of reliability that is demanded and expected of a service like BigQuery and apologize for the disruption.  We are taking immediate actions to ensure we minimize the risk of this issue repeating itself.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 7 May 2015 from 20:45 to 21:20 PDT and on Friday 8 May from 03:13 to 04:47, requests to the Web UI resulted in the page hanging with the message âLoading BigQueryâ¦â.  Additionally, when accessing BigQuery via the API, users would have seen responses with error code 400 or 500.
## ROOT CAUSE:
A routine software upgrade to the authorization process in BigQuery had a side effect of reducing the cache hit rate of dataset permission validation.  A particular query load triggered a cascade of live authorization checks that fanned out and amplified throughout the BigQuery service, eventually causing user visible errors as the authorization backends became overwhelmed.  As a byproduct, error rates for the service increased as individual requests failed to authorize.
REMEDIATION AND PREVENTION:
Google engineers were able to identify and cancel problematic in-flight BigQuery queries that were causing a high number of retries to the permissions validation backend.  To prevent a recurrence of this issue, engineers temporarily disabled the retry of these queries to prevent retries from amplifying the effect of unhealthy permission validation backends.  Google engineers were also able to adjust the retry parameters of the authorization system to return cache hit rates to normal.   As the system stabilized, BigQuery engineers were able to gradually allow query traffic to flow in and re-enabled permission validation, restoring service.
To prevent future recurrences of this issue, Google engineers will change the structure of permissions validation so that continual retries will not destabilize the entire service.  This restructuring includes reducing the number of backends that require permissions validation by changing the steps involved in the BigQuery request validation process.  Engineers will also introduce safety limits governing communication between BigQuery and the permissions validation system.  Google engineers are also adding additional monitoring to better detect and potentially preemptively mitigate issues of this nature.

# [bigquery/18012](https://status.cloud.google.com/incident/bigquery/18012)
12:53 Dec 01, 2015
## SUMMARY:
On Sunday 29th of November 2015, for an aggregate of 33 minutes occurring between 7:31am and 8:24am PST, 11% of all requests to the BigQuery API experienced errors. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we have taken and are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Sunday 29th of November 2015, between 7:31am and 7:41am, 7% of BigQuery API requests were redirected (HTTP 302) to a CAPTCHA service. The issue reoccurred between 8:01am and 8:24am PST, affecting 22% of requests. As the CAPTCHA service is intended to verify that the requester is human, any automated requests that were redirected failed.
## ROOT CAUSE:
The BigQuery API is designed to provide fair service to all users during intervals of unusually-high traffic.  During this event, a surge in traffic to the API caused traffic verification and fairness systems to activate, causing a fraction of requests to be redirected to the CAPTCHA service.
REMEDIATION AND PREVENTION:
While investigating the source of the increased traffic, Google engineers assessed that BigQueryâs service capacity was sufficient to handle the additional queries without putting existing queries at risk.  The engineers instructed BigQuery to allow the additional queries without verification, ending the incident.
To prevent future recurrences of this problem, Google engineers will change BigQuery's traffic threshold policy to an adaptive mechanism appropriate for automated requests, which provides intelligent traffic control and isolation for individual users.

# [bigquery/18015](https://status.cloud.google.com/incident/bigquery/18015)
09:38 Jun 01, 2016
## SUMMARY:
On Wednesday 18 May 2016 the BigQuery API was unavailable for two periods totaling 31 minutes. We understand how important access to your data stored in BigQuery is and we apologize for the impact this had on you. We have investigated the incident to determine how we can mitigate future issues and provide better service for you in the future.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 18 May 2016 from 11:50 until 12:15 PDT all non-streaming BigQuery API calls failed, and additionally from 14:41 until 14:47, 70% of calls failed. An error rate of 1% occurred from 11:28 until 15:34. API calls affected by this issue experienced elevated latency and eventually returned an HTTP 500 status with an error message of "Backend Error". The BigQuery web console was also unavailable during these periods.
The streaming API and BigQuery export of logs and usage data were unaffected.
## ROOT CAUSE:
In 2015 BigQuery introduced datasets located in Europe. This required infrastructure to allow BigQuery API calls to be routed to an appropriate zone. This infrastructure was deployed uneventfully and has been operating in production for some time.  The errors on 18 May were caused when a new configuration was deployed to improve routing of APIs, and then subsequently rolled back.  The engineering team has made changes to the routing configuration for BigQuery API calls to prevent this issue from recurring in the future, and to more rapidly detect elevated error levels in BigQuery API calls in the future
Finally, we would like to apologize for this issue - particularly its scope and duration. We know that BigQuery is a critical component of many GCP deployments, and we are committed to continually improving its availability.

# [bigquery/18018](https://status.cloud.google.com/incident/bigquery/18018)
16:06 Jul 27, 2016
## SUMMARY:
On Monday 25 July 2016, the Google BigQuery Streaming API experienced elevated error rates for a duration of 71 minutes. We apologize if your service or application was affected by this and we are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Monday 25 July 2016 between 17:03 and 18:14 PDT, the BigQuery Streaming API returned HTTP 500 or 503 errors for 35% of streaming insert requests, with a peak error rate of 49% at 17:40. Customers who retried on error were able to mitigate the impact.
Calls to the BigQuery jobs API showed an error rate of 3% during the incident but could generally be executed reliably with normal retry behaviour. Other BigQuery API calls were not affected.
## ROOT CAUSE:
An internal Google service sent an unexpectedly high amount of traffic to the BigQuery Streaming API service. The internal service used a different entry point that was not subject to quota limits. Google's internal load balancers drop requests that exceed the capacity limits of a service. In this case, the capacity limit for the Streaming API service had been configured higher than its true capacity. As a result, the internal Google service was able to send too many requests to the Streaming API, causing it to fail for a percentage of responses.
The Streaming API service sends requests to BigQuery's Metadata service in order to handle incoming Streaming requests. This elevated volume of requests exceeded the capacity of the Metadata service which resulted in errors for BigQuery jobs API calls.
REMEDIATION AND PREVENTION:
The incident started at 17:03. Our monitoring detected the issue at 17:20 as error rates started to increase. Our engineers blocked traffic from the internal Google client causing the overload shortly thereafter which immediately started to mitigate the impact of the incident. Error rates dropped to normal by 18:14.
In order to prevent a recurrence of this type of incident we will enforce quotas for internal Google clients on requests to the Streaming service in order to prevent a single client sending too much traffic. We will also set the correct capacity limits for the Streaming API service based on improved load tests in order to ensure that internal clients cannot exceed the service's capacity.
We apologize again to customers impacted by this incident.

# [bigquery/18021](https://status.cloud.google.com/incident/bigquery/18021)
15:42 Oct 23, 2014
## SUMMARY:
On Wednesday 22 October 2014, some users of Google BigQuery, Google Cloud Storage and the Google Developers Console experienced elevated error rates for a period of 62 minutes. We apologize if your service or application was affected. We take these incidents extremely seriously and are taking immediate steps to ensure that this type of incident does not happen again.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 22 October 2014 from 14:30 to 15:32 PDT the following Google Cloud Platform services experienced elevated error rates: the Developers Console experienced a 96% error rate; BigQuery experienced a 45% error rate; and Cloud Storage experienced a 6.0% error rate for the XML API and a 3.4% error rate for the JSON API.
## ROOT CAUSE:
The incident occurred when Googleâs internal project metadata store experienced elevated latency, which was caused by an internal system writing to the metadata store at a higher rate than normal. BigQuery, Cloud Storage and the Developers Console frequently need to read project metadata in order to handle requests.
REMEDIATION AND PREVENTION:
Google engineers detected the incident at 14:36. We identified the root cause as the project metadata store at 14:58. At 15:06, we disabled the component of the metadata store that was responsible for the increased latency. The rollout of this fix was completed by 15:32.
In order to prevent future problems of this nature from happening again, we will fix the performance issue in the metadata store that caused its latency to increase when under higher load. For Cloud Storage and BigQuery, we will improve caching of project metadata so that a failure of the metadata store has less impact on the service. We will also make monitoring improvements to get earlier detection and faster diagnosis of problems with the metadata store.

# [bigquery/18022](https://status.cloud.google.com/incident/bigquery/18022)
12:14 Nov 11, 2016
## SUMMARY:
On Tuesday 8 November 2016, Google BigQueryâs streaming service, which includes streaming inserts and queries against recently committed streaming buffers, was largely unavailable for a period of 4 hours and 11 minutes. To our BigQuery customers whose business analytics were impacted during this outage, we sincerely apologize. We will be providing an SLA credit for the affected timeframe. We have conducted an internal investigation and are taking steps to improve our service.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 8 November 2016 from 16:00 to 20:11 US/Pacific, 73% of BigQuery streaming inserts failed with a 503 error code indicating an internal error had occurred during the insertion.  At peak, 93% of BigQuery streaming inserts failed.  During the incident, queries performed on tables with recently-streamed data returned a result code (400) indicating that the table was unavailable for querying. Queries against tables in which data were not streamed within the 24 hours preceding the incident were unaffected. There were no issues with non-streaming ingestion of data.
## ROOT CAUSE:
The BigQuery streaming service requires authorization checks to verify that it is streaming data from an authorized entity to a table that entity has permissions to access.  The authorization service relies on a caching layer in order to reduce the number of calls to the authorization backend.  At 16:00 US/Pacific, a combination of reduced backend authorization capacity coupled with routine cache entry refreshes caused a surge in requests to the authorization backends, exceeding their current capacity.  Because BigQuery does not cache failed authorization attempts, this overload meant that new streaming requests would require re-authorization, thereby further increasing load on the authorization backend.  This continual increase of authorization requests on an already overloaded authorization backend resulted in continued and sustained authorization failures which propagated into streaming request and query failures.
REMEDIATION AND PREVENTION:
Google engineers were alerted to issues with the streaming service at 16:21 US/Pacific.  Their initial hypothesis was that the caching layer for authorization requests was failing. The engineers started redirecting requests to bypass the caching layer at 16:51.  After testing the system without the caching layer, the engineers determined that the caching layer was working as designed, and requests were directed to the caching layer again at 18:12.  At 18:13, the engineering team was able to pinpoint the failures to a set of overloaded authorization backends and begin remediation.
The issue with authorization capacity was ultimately resolved by incrementally reducing load on the authorization system internally and increasing the cache TTL, allowing streaming authorization requests to succeed and populate the cache so that internal services could be restarted.  Recovery of streaming errors began at 19:34 US/Pacific and the streaming service was fully restored at 20:11.
To prevent short-term recurrence of the issue, the engineering team has greatly increased the request capacity of the authorization backend.
In the longer term, the BigQuery engineering team will work on several mitigation strategies to address the currently cascading effect of failed authorization requests.  These strategies include caching intermediary responses to the authorization flow for the streaming service, caching failure states for authorization requests and adding rate limiting to the authorization service so that large increases in cache miss rate will not overwhelm the authorization backend.
In addition, the BigQuery engineering team will be improving the monitoring of available capacity on the authorization backend and will add additional alerting so capacity issues can be mitigated before they become cascading failures.  The BigQuery engineering team will also be investigating ways to reduce the spike in authorization traffic that occurs daily at 16:00 US/Pacific when the cache is rebuilt to more evenly distribute requests to the authorization backend.
Finally, we have received feedback that our communications during the outage left a lot to be desired. We agree with this feedback. While our engineering teams launched an all-hands-on-deck to resolve this issue within minutes of its detection, we did not adequately communicate both the level-of-effort and the steady progress of diagnosis, triage and restoration happening during the incident. We clearly erred in not communicating promptly, crisply and transparently to affected customers during this incident. We will be addressing our communications â for all Google Cloud systems, not just BigQuery â as part of a separate effort, which has already been launched.
We recognize the extended duration of this outage, and we sincerely apologize to our BigQuery customers for the impact to your business analytics.

# [bigquery/18026](https://status.cloud.google.com/incident/bigquery/18026)
15:55 Mar 15, 2017
## ISSUE SUMMARY:
On Monday 13 March 2017, the BigQuery streaming API experienced 91% error rate in the US and 63% error rate in the EU for a duration of 30 minutes. We apologize for the impact of this issue on our customers, and the widespread nature of the issue in particular. We have completed a post mortem of the incident and are making changes to mitigate and prevent recurrences.
## DETAILED DESCRIPTION OF IMPACT:
On Monday 13 March 2017 from 10:22 to 10:52 PDT 91% of streaming API requests to US BigQuery datasets and 63% of streaming API requests to EU BigQuery datasets failed with error code 503 and an HTML message indicating "We're sorry... but your computer or network may be sending automated queries. To protect our users, we can't process your request right now."
All non-streaming API requests, including DDL requests and query, load extract and copy jobs were unaffected.
## ROOT CAUSE:
The trigger for this incident was a sudden increase in log entries being streamed from Stackdriver Logging to BigQuery by logs export. The denial of service (DoS) protection used by BigQuery responded to this by rejecting excess streaming API traffic. However the configuration of the DoS protection did not adequately segregate traffic streams resulting in normal sources of BigQuery streaming API requests being rejected.
REMEDIATION AND PREVENTION
Google engineers initially mitigated the issue by blocking the source of unexpected load. This prevented the overload and allowed all other traffic to resume normally. Engineers fully resolved the issue by identifying and reverting the change that triggered the increase in log entries and clearing the backlog of log entries that had grown.
To prevent future occurrences, BigQuery engineers are updating configuration to increase isolation between different traffic sources. Tests are also being added to verify behavior under several new load scenarios.

# [bigquery/18029](https://status.cloud.google.com/incident/bigquery/18029)
23:25 Jun 20, 2017
## ISSUE SUMMARY:
For 10 minutes on Wednesday 14 June 2017, Google BigQuery experienced increased error rates for both streaming inserts and most API methods due to their dependency on metadata read operations. To our BigQuery customers whose business were impacted by this event, we sincerely apologize. We are taking immediate steps to improve BigQueryâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
Starting at 10:43am US/Pacific, global error rates for BigQuery streaming inserts and API calls dependent upon metadata began to rapidly increase. The error rate for streaming inserts peaked at 100% by 10:49am. Within that same window, the error rate for metadata operations increased to a height of 80%. By 10:54am the error rates for both streaming inserts and metadata operations returned to normal operating levels.
During the incident, affected BigQuery customers would have experienced a noticeable elevation in latency on all operations, as well as increased âService Unavailableâ and âTimeoutâ API call failures. While BigQuery streaming inserts and metadata operations were the most severely impacted, other APIs also exhibited elevated latencies and error rates, though to a much lesser degree. For API calls returning status code 2xx the operation completed with successful data ingestion and integrity.
## ROOT CAUSE:
On Wednesday 14 June 2017, BigQuery engineers completed the migration of BigQuery's metadata storage to an improved backend infrastructure. This effort was the culmination of work to incrementally migrate BigQuery read traffic over the course of two weeks. As the new backend infrastructure came online, there was one particular type of read traffic that hadnât yet migrated to the new metadata storage. This caused a sudden spike of that read traffic to the new backend.
The spike came when the new storage backend had to process a large volume of incoming requests as well as allocate resources to handle the increased load. Initially the backend was able to process requests with elevated latency, but all available resources were eventually exhausted, which lead to API failures. Once the backend was able to complete the load redistribution, it began to free up resources to process existing requests and work through its backlog. BigQuery operations continued to experience elevated latency and errors for another five minutes as the large backlog of requests from the first five minutes of the incident were processed.
REMEDIATION AND PREVENTION
Our monitoring systems worked as expected and alerted us to the outage within 6 minutes of the error spike. By this time, the underlying root cause had already passed.
Google engineers have created nine high priority action items, and three lower priority action items as a result of this event to better prevent, detect and mitigate the reoccurence of a similar event.
The most significant of these priorities is to modify the BigQuery service to successfully handle a similar root cause event. This will include adjusting capacity parameters to better handle backend failures and improving caching and retry logic.
Each of the 12 action items created from this event have already been assigned to an engineer and are underway.

# [bigquery/18030](https://status.cloud.google.com/incident/bigquery/18030)
23:02 Jul 10, 2017
## ISSUE SUMMARY:
On Wednesday 28 June 2017, streaming data into Google BigQuery experienced elevated error rates for a period of 57 minutes.  We apologize to all users whose data ingestion pipelines were affected by this issue.  We understand the importance of reliability for a process as crucial as data ingestion and are taking committed actions to prevent a similar recurrence in the future.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 28 June 2017 from 18:00 to 18:20 and from 18:40 to 19:17 US/Pacific time, BigQuery's streaming insert service returned an increased error rate to clients for all projects.  The proportion varied from time to time, but failures peaked at 43% of streaming requests returning HTTP response code 500 or 503.  Data streamed into BigQuery from clients that experienced errors without retry logic were not saved into target tables during this period of time.
## ROOT CAUSE:
Streaming requests are routed to different datacenters for processing based on the table ID of the destination table. A sudden increase in traffic to the BigQuery streaming service combined with diminished capacity in a datacenter resulted in that datacenter returning a significant amount of errors for tables whose IDs landed in that datacenter.  Other datacenters processing streaming data into BigQuery were unaffected.
REMEDIATION AND PREVENTION
Google engineers were notified of the event at 18:20, and immediately started to investigate the issue. The first set of errors had subsided, but starting at 18:40 error rates increased again. At 19:17 Google engineers redirected traffic away from the affected datacenter. The table IDs in the affected datacenter were redistributed to remaining, healthy streaming servers and error rates began to subside.
To prevent the issue from recurring, Google engineers are improving the load balancing configuration, so that spikes in streaming traffic can be more equitably distributed amongst the available streaming servers.  Additionally, engineers are adding further monitoring as well as tuning existing monitoring to decrease the time it takes to alert engineers of issues with the streaming service.  Finally, Google engineers are evaluating rate-limiting strategies for the backend to prevent them from becoming overloaded.

# [bigquery/18032](https://status.cloud.google.com/incident/bigquery/18032)
08:12 Aug 02, 2017
## ISSUE SUMMARY:
On 2017-07-26, BigQuery delivered error messages for 7% of queries and 15% of exports for a duration of two hours and one minute. It also experienced elevated failures for streaming inserts for one hour and 40 minutes. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we are taking immediate steps to improve BigQueryâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On 2017-07-26 from 13:45 to 15:45 US/PDT, BigQuery jobs experienced elevated failures at a rate of 7% to 15%, depending on the operation attempted. Overall 7% of queries, 15% of exports, and 9% of streaming inserts failed during this event. These failures occurred in 12% of customer projects The errors for affected projects varied from 2% to 69% of exports, over 50% for queries, and up to 28.5% for streaming inserts.  Customers affected saw an error message stating that their project has ânot enabled BigQueryâ.
## ROOT CAUSE:
Prior to executing a BigQuery job, Googleâs Service Manager validates that the project requesting the job has BigQuery enabled for the project. The Service Manager consists of several components, including a redundant data store for project configurations, and a permissions module which inspects configurations. The project configuration data is being migrated to a new format and new version of the data store, and as part of that migration, the permissions module is being updated to use the new format. As is normal production best practices, this migration is being performed in stages separated by time.
The root cause of this event was that, during one stage of the rollout, configuration data for two GCP datacenters was migrated before the corresponding permissions module for BigQuery was updated. As a result, the permissions module in those datacenters began erroneously reporting that projects running there no longer had BigQuery enabled. Thus, while both BigQuery and the underlying data stores were unchanged, requests to BigQuery from affected projects received an error message indicating that they had not enabled BigQuery.
REMEDIATION AND PREVENTION
Googleâs BigQuery on-call engineering team was alerted by automated monitoring within 15 minutes of the beginning of the event at 13:59.  Subsequent investigation determined at 14:17 that multiple projects were experiencing BigQuery validation failures, and the cause of the errors was identified at 14:46 as being changed permissions.
Once the root cause of the errors was understood, Google engineers focused on mitigating the user impact by configuring BigQuery in affected locations to skip the erroneous permissions check. This change was first tested in a portion of the affected projects beginning at 15:04, and confirmed to be effective at 15:29.  That mitigation was then rolled out to all affected projects, and was complete by 15:44. Finally, with mitigations in place, the Google engineering team worked to safely roll back the data migration; this work completed at 23:33 and the permissions check mitigation was removed, closing the incident.
Google engineering has created 26 high priority action items to prevent a recurrence of this condition and to better detect and more quickly mitigate similar classes of issues in the future.  These action items include increasing the auditing of BigQueryâs use of Googleâs Service Manager, improving the detection and alerting of the conditions that caused this event, and improving the response of Google engineers to similar events. In addition, the core issue that affected the BigQuery backend has already been fixed.
Google is committed to quickly and continually improving our technology and operations to prevent service disruptions. We appreciate your patience and apologize again for the impact to your organization.

# [bigquery/18036](https://status.cloud.google.com/incident/bigquery/18036)
14:34 May 18, 2018
## ISSUE SUMMARY:
On Wednesday 16 May 2018, Google BigQuery experienced failures of import, export and query jobs for a duration of 88 minutes over two time periods (55 minutes initially, and 33 minutes in the second, which was isolated to the EU). We sincerely apologize to all of our affected customers; this is not the level of reliability we aim to provide in our products. We will be issuing SLA credits to customers who were affected by this incident and we are taking immediate steps to prevent a future recurrence of these failures.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 16 May 2018 from 16:00 to 16:55 and from to 17:45 to 18:18 PDT, Google BigQuery experienced a failure of some import, export and query jobs. During the first period of impact, there was a 15.26% job failure rate; during the second, which was isolated to the EU, there was a 2.23% error rate. Affected jobs would have failed with INTERNAL_ERROR as the reason.
## ROOT CAUSE:
Configuration changes being rolled out on the evening of the incident were not applied in the intended order. This resulted in an incomplete configuration change becoming live in some zones, subsequently triggering the failure of customer jobs. During the process of rolling back the configuration, another incorrect configuration change was inadvertently applied, causing the second batch of job failures.
REMEDIATION AND PREVENTION
Automated monitoring alerted engineering teams 15 minutes after the error threshold was met and were able to correlate the errors with the configuration change 3 minutes later. We feel that the configured alert delay is too long and have lowered it to 5 minutes in order to aid in quicker detection.
During the rollback attempt, another bad configuration change was enqueued for automatic rollout and when unblocked, proceeded to roll out, triggering the second round of job failures. To prevent this from happening in the future, we are working to ensure that rollouts are automatically switched to manual mode when engineers are responding to production incidents.
In addition, we're switching to a different configuration system which will ensure the consistency of configuration at all stages of the rollout.

# [bigquery/18037](https://status.cloud.google.com/incident/bigquery/18037)
09:22 Jun 27, 2018
## ISSUE SUMMARY:
On Friday 22 June 2018, Google BigQuery experienced increased query failures for a duration of 1 hour 6 minutes. We apologize for the impact of this issue on our customers and are making changes to mitigate and prevent a recurrence.
## DETAILED DESCRIPTION OF IMPACT:
On Friday 22 June 2018 from 12:06 to 13:12 PDT, up to 50% of total requests to the BigQuery API failed with error code 503. Error rates varied during the incident, with some customers experiencing 100% failure rate for their BigQuery table jobs. bigquery.tabledata.insertAll jobs were unaffected.
## ROOT CAUSE:
A new release of the BigQuery API introduced a software defect that caused the API component to return larger-than-normal responses to the BigQuery router server. The router server is responsible for examining each request, routing it to a backend server, and returning the response to the client. To process these large responses, the router server allocated more memory which led to an increase in garbage collection. This resulted in an increase in CPU utilization, which caused our automated load balancing system to shrink the server capacity as a safeguard against abuse. With the reduced capacity and now comparatively large throughput of requests, the denial of service protection system used by BigQuery responded by rejecting user requests, causing a high rate of 503 errors.
REMEDIATION AND PREVENTION
Google Engineers initially mitigated the issue by increasing the capacity of the BigQuery router server which prevented overload and allowed API traffic to resume normally. The issue was fully resolved by identifying and reverting the change that caused large response sizes.
To prevent future occurrences, BigQuery engineers will also be adjusting capacity alerts to improve monitoring of server overutilization.
We apologize once again for the impact of this incident on your business.

# [bigquery/19002](https://status.cloud.google.com/incident/bigquery/19002)
11:25 Mar 18, 2019
## ISSUE SUMMARY:
On Friday 8 March 2019, Google BigQueryâs jobs.insert API in the US regions experienced an average elevated error rate of 51.21% for a duration of 45 minutes. BigQueryâs Streaming API was unaffected during this period. We understand how important BigQueryâs availability is to our customersâ business analytics and we sincerely apologize for the impact caused by this incident. We are taking immediate steps detailed below to prevent this situation from happening again.
## DETAILED DESCRIPTION OF IMPACT:
On Friday 8 March 2019 from 00:45 - 01:30 US/Pacific, BigQueryâs jobs.insert [1] API (responsible for import/export, query, and copy jobs) in the US region experienced an average error rate of 51.21%. Affected customers received error responses such as âError encountered during Execution, retrying may solve the problemâ and âRead timed outâ when sending requests to BigQuery. BigQueryâs Streaming API was not impacted by this incident.
The following is a breakdown of the errors experienced during the incident:

64.01% of jobs.insert API requests to BigQuery (US) received HTTP 503 errors
The jobs.insert API experienced an average error rate of 51.21% and a peak error rate of 75.96% percent at 01:21 US/Pacific
17.93% of BigQuery projects in the region were impacted

## ROOT CAUSE:
A recent change to BigQueryâs shuffle scheduling service [2] introduced the potential for the service to enter a state where it was unable to process shuffle jobs. A new canary release was deployed to fix the potential issue. However, this release contained an unrelated issue which placed an overly restrictive rate limit on the shuffle service preventing it from operating nominally. This strict rate limit created a large job backlog for the BigQuery Job Server, which resulted in BigQuery returning errors such as âError encountered during Execution, retrying may solve the problemâ and âRead timed outâ to users.
REMEDIATION AND PREVENTION
Google Engineers were automatically alerted at 00:47 and immediately began their investigation. The root cause was discovered at 01:23, and our engineers worked quickly to mitigate the issue by redirecting traffic away from the impacted datacenter at 01:27. The incident was fully resolved by 01:30.
We are taking immediate action to prevent recurrence. First, we have implemented a fix to prevent the shuffle service from potentially entering a state where it is unable to process jobs. Second, we are allocating additional capacity to BigQueryâs US region to reduce the impact of traffic redirections on adjacent datacenters running the service. Additionally, we are increasing the precision of our monitoring to enable more swift and accurate diagnosing of BigQuery issues going forward.
[1] https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert
[2] https://cloud.google.com/blog/products/gcp/in-memory-query-execution-in-google-bigquery

# [bigquery/19003](https://status.cloud.google.com/incident/bigquery/19003)
21:00 May 23, 2019
## ISSUE SUMMARY:
On Friday, May 17 2019, 83% of Google BigQuery insert jobs in the US multi-region failed for a duration of 27 minutes. Query jobs experienced an average error rate of 16.7% for a duration of 2 hours. BigQuery users in the US multi-region also observed elevated latency for a duration of 4 hours and 40 minutes. To our BigQuery customers whose business analytics were impacted during this outage, we sincerely apologize â this is not the level of quality and reliability we strive to offer you, and we are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Friday May 17 2019, from 08:30 to 08:57 US/Pacific, 83% of Google BigQuery insert jobs failed for 27 minutes in the US multi-region. From 07:30 to 09:30 US/Pacific, query jobs in US multi-region returned an average error rate of 16.7%. Other jobs such as list, cancel, get, and getQueryResults in the US multi-region were also affected for 2 hours along with query jobs. Google BigQuery users observed elevated latencies for job completion from 07:30 to 12:10 US/Pacific. BigQuery jobs in regions outside of the US remained unaffected.
## ROOT CAUSE:
The incident was triggered by a sudden increase in queries in US multi-region leading to quota exhaustion in the storage system serving incoming requests. Detecting the sudden increase, BigQuery initiated its auto-defense mechanism and redirected user requests to a different location. The high load of requests triggered an issue in the scheduling system, causing delays in scheduling incoming queries. These delays resulted in errors for query, insert, list, cancel, get and getQueryResults BigQuery jobs and overall latency experienced by users. As a result of these high number of requests at 08:30 US/Pacific, the scheduling systemâs overload protection mechanism began rejecting further incoming requests, causing insert job failures for 27 minutes.
REMEDIATION AND PREVENTION
BigQueryâs defense mechanism began redirection at 07:50 US/Pacific. Google Engineers were automatically alerted at 07:54 US/Pacific and began investigation. The issue with the scheduler system began at 08:00 and our engineers were alerted again at 08:10. At 08:43, they restarted the scheduling system which mitigated the insert job failures by 08:57. Errors seen for insert, query, cancel, list, get and getQueryResults jobs  were mitigated by 09:30 when queries were redirected to different locations. Google engineers then successfully blocked the source of sudden incoming queries that helped reduce overall latency. The issue was fully resolved at 12:10 US/Pacific when all active and pending queries completed running.
We will resolve the issue that caused the scheduling system to delay scheduling of incoming queries. Although the overload protection mechanism prevented the incident from spreading globally, it did cause the failures for insert jobs. We will be improving this mechanism by lowering deadline for synchronous queries which will help prevent queries from piling up and overloading the scheduling system.  To prevent future recurrence of the issue we will also implement changes to improve BigQueryâs quota exhaustion behaviour that would prevent the storage system to take on more load than it can handle. To reduce the duration of similar incidents, we will implement tools to quickly remediate backlogged queries.

# [cloud/dataflow/16001](https://status.cloud.google.com/incident/cloud/dataflow/16001)
15:29 Aug 18, 2016
## SUMMARY:
On Friday 12 August 2016, Cloud Dataflow experienced pipeline delays for 99 minutes. Although all pipelines did eventually successfully complete, we know that you rely on the timely execution of these flows and apologise for the long duration and impact of this incident. We are taking steps to improve reliability and time to resolution so that we meet the level of service that you rightly expect.
## DETAILED DESCRIPTION OF IMPACT:
On Friday 12 August 2016 13:29 to 15:08 PDT all Dataflow pipelines ceased to process data, but remained in "Running" state. Requests to start new Dataflow pipelines or cancel existing ones failed. After the period of impact, existing pipelines resumed processing without missing any input data.
## ROOT CAUSE:
During mitigation of a lower impact performance issue, Google engineers made a configuration change to pipeline orchestration. An error in this configuration caused validation within the orchestration component to reject all requests. As calls to this component are needed to create jobs, cancel jobs and make progress on existing jobs, none of these operations were possible.
REMEDIATION AND PREVENTION:
At 14:59 Google engineers rolled back the erroneous configuration change, a few minutes after which errors ceased and normal pipeline execution resumed.
In future Dataflow configuration changes will go through additional validation in the form of  pre-deployment tests, staging and progressive rollouts. This defense in depth will minimize the possible impact of future errors.
To improve detection and isolation time, Dataflow servers are being altered to abort if started with invalid configuration. This provides a strong signal that can be used in automated systems and is fast for engineers to identify. Additionally we are improving our availability alerting such that elevated error rates on all operations will notify engineers of problems more quickly.
We apologize for the difficulty this issue caused you.

# [cloud/datastore/17002](https://status.cloud.google.com/incident/cloud/datastore/17002)
14:00 Feb 21, 2017
## ISSUE SUMMARY:
On Tuesday 14 February 2017, some applications using Google Cloud Datastore in Western Europe or the App Engine Search API in Western Europe experienced 2%-4% error rates and elevated latency for three periods with an aggregate duration of three hours and 36 minutes. We apologize for the disruption this caused to your service. We have already taken several measures to prevent incidents of this type from recurring and to improve the reliability of these services.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 14 February 2017 between 00:15 and 01:18 PST, 54% of applications using Google Cloud Datastore in Western Europe or the App Engine Search API in Western Europe experienced elevated error rates and latency. The average error rate for affected applications was 4%.
Between 08:35 and 08:48 PST, 50% of applications using Google Cloud Datastore in Western Europe or the App Engine Search API in Western Europe experienced elevated error rates. The average error rate for affected applications was 4%.
Between 12:20 and 14:40 PST, 32% of applications using Google Cloud Datastore in Western Europe or the App Engine Search API in Western Europe experienced elevated error rates and latency. The average error rate for affected applications was 2%.
Errors received by affected applications for all three incidents were either "internal error" or "timeout".
## ROOT CAUSE:
The incident was caused by a latent bug in a service used by both Cloud Datastore and the App Engine Search API that was triggered by high load on the service.
Starting at 00:15 PST, several applications changed their usage patterns in one zone in Western Europe and began running more complex queries, which caused higher load on the service.
REMEDIATION AND PREVENTION
Google's monitoring systems paged our engineers at 00:35 PST to alert us to elevated errors in a single zone. Our engineers followed normal practice, by redirecting traffic to other zones to reduce the impact on customers while debugging the underlying issue. At 01:15, we redirected traffic to other zones in Western Europe, which resolved the incident three minutes later.
At 08:35 we redirected traffic back to the zone that previously had errors. We found that the error rate in that zone was still high and so redirected traffic back to other zones at 08:48.
At 12:45, our monitoring systems detected elevated errors in other zones in Western Europe. At 14:06 Google engineers added capacity to the service with elevated errors in the affected zones. This removed the trigger for the incident.
We have now identified and fixed the latent bug that caused errors when the system was at high load. We expect to roll out this fix over the next few days.
Our capacity planning team have generated forecasts for peak load generated by the Cloud Datastore and App Engine Search API and determined that we now have sufficient capacity currently provisioned to handle peak loads.
We will be making several changes to our monitoring systems to improve our ability to quickly detect and diagnose errors of this type.
Once again, we apologize for the impact of this incident on your application.

# [cloud/datastore/19001](https://status.cloud.google.com/incident/cloud/datastore/19001)
14:00 Feb 14, 2019
## ISSUE SUMMARY:
Cloud Datastore experienced a low rate of errors associated with a small subset of high write-rate databases. We have separately notified the customers who may have been potentially impacted by these errors.
## DETAILED DESCRIPTION OF IMPACT:
Beginning Wednesday December 19, 2018 and ending January 19 2019, Cloud Datastore experienced a low rate of errors associated with a small subset of high write-rate databases. Less than 0.1% of databases may have experienced these errors when called from the us-central1 region. We have separately notified the customers who may have been potentially impacted by these errors.
REMEDIATION AND PREVENTION
We have identified and remediated the issue. As part of the remediation, we reverted to an earlier rollout ending the event. After verifying the issue was resolved, Google is taking steps to improve our existing testing scenarios to help prevent future recurrence.

# [cloud/iam/18001](https://status.cloud.google.com/incident/cloud/iam/18001)
09:20 Jul 02, 2018
## ISSUE SUMMARY:
On Wednesday 27 June 2018, Google Cloud Console and Google Cloud Resource Manager API experienced a significant performance degradation for a duration of 51 minutes. Although, this did not affect user resources running on the Google Cloud Platform, we understand that our customers rely heavily on Google Cloud Console to manage their resources and we sincerely apologize to everyone who was affected by the incident.
## DETAILED DESCRIPTION OF IMPACT:
From 14:21 to 15:11 PDT, users were unable to manage their folders, projects and organizations using Google Cloud Console, Google Cloud Resource Manager API and gcloud command line. The following APIs were affected:
Google Cloud Console: Impacted users were unable to list their projects, search for projects, folders and organizations or view their bill. Search box failed to return the above too.
Google Cloud Resource Manager API: Impacted users were unable to list their projects, folders and organizations
BigQuery: Impacted users were unable to list their bigquery projects using the API.
## ROOT CAUSE:
The incident was triggered by a configuration change in the search infrastructure powering Cloud resource metadata search. The search infrastructure sends ACL checks to a central ACL server to make sure the end user has access to the Cloud resource metadata it plans to return. The configuration change introduced a new field in the ACL check request, while the central ACL server had not whitelisted the search infrastructure to send that field, causing an outage in Cloud resource metadata search.
REMEDIATION AND PREVENTION
At 12:26 PDT, Google Engineers rolled out the configuration change. Our automated release validation system rejected the change due to a high rate of errors. Around 14:16 PDT, an unrelated change was made to the same search infrastructure which triggered a bug that disabled its automated release validation system. This change also inadvertently picked up the prior configuration change and due to the lack of automated release validation, the change was successfully propagated to production.  Within a span of few minutes, several engineering teams were automatically alerted to the situation and began the mitigation process.
The issue was fully mitigated at 15:11 PDT when the configuration change was rolled back.
We apologize again for the inconvenience caused. We are taking immediate steps to prevent recurrence and improve reliability in the future, including:
Fixing the bug that inadvertently disabled the canary analysis system.
Improving process around pushing changes that involve several dependencies.
Improving testing and staging alerts to catch issues of this nature before they reach production.

# [cloud/networking/17002](https://status.cloud.google.com/incident/cloud/networking/17002)
17:16 Sep 05, 2017
Revised Tuesday 05 September 2017 to clarify the impact and timing.
## ISSUE SUMMARY:
For portions of Tuesday 29 August and Wednesday 30 August 2017, some Google Compute Engine instances which were live migrated from one server to another stopped receiving network traffic from Google Cloud Network Load Balancers and Internal Load balancers. On average, less than 1% of GCE instances were affected by this behavior over the duration of the incident, and at its peak, 2% of instances were affected. For the 2% of instances which were ultimately affected, the mean duration of the impact was 9 hours and the maximum duration was 30 hours and 22 minutes. We apologize for the impact this had on your services. We are particularly cognizant of the unusual duration of the incident. We have completed an extensive postmortem to learn from the issue and improve Google Cloud Platform.
## DETAILED DESCRIPTION OF IMPACT:
Any GCE instance that was live-migrated between 13:56 PDT on Tuesday 29 August 2017 and 08:32 on Wednesday 30 August 2017 became unreachable via Google Cloud Network or Internal Load Balancing until between 08:56 and 14:18 (for regions other than us-central1) or 20:16 (for us-central1) on Wednesday. See https://goo.gl/NjqQ31 for a visual representation of the cumulative number of instances live-migrated over time.
Our internal investigation shows that, at peak, 2% of GCE instances were affected by the issue.
Instances which were not live-migrated during this period were not affected. In addition, instances that do not use Network Load Balancing or Internal Load Balancing were not affected. Related capabilities such as Google Cloud HTTP(S) Load Balancing, TCP and SSL Proxy Load Balancing and direct connectivity on instance internal and external IP addresses were unaffected.
## ROOT CAUSE:
Live-migration transfers a running VM from one host machine to another host machine within the same zone. All VM properties and attributes remain unchanged, including internal and external IP addresses, instance metadata, block storage data and volumes, OS and application state, network settings, network connections, and so on.
In this case, a change in the internal representation of networking information in VM instances caused inconsistency between two values, both of which were supposed to hold the external and internal virtual IP addresses of load balancers. When an affected instance was live-migrated, the instance was deprogrammed from the load balancer because of the inconsistency.  This made it impossible for load balancers that used the instance as backend to look up the destination IP address of the instance following its migration, so traffic destined for that instance was not forwarded from the load balancer.
REMEDIATION AND PREVENTION
At 08:32 Google engineers rolled back the triggering change, at which point no new live-migration would cause the issue.  At 08:56 they then started a process which fixed all mismatched network information; this process completed at 14:18 except for us-central1 which took until 20:18.
In order to prevent the issue from recurring, Google engineers are enhancing the automated canary testing that simulates live-migration events, increasing detection of load balancing packets loss, and enforcing more restrictions on new configuration changes deployment for internal representation changes.

# [cloud/networking/18003](https://status.cloud.google.com/incident/cloud/networking/18003)
16:42 Feb 16, 2018
## ISSUE SUMMARY:
On Sunday 18 January 2018, Google Compute Engine networking experienced a network programming failure.  The two impacts of this incident included the autoscaler not scaling instance groups, as well as migrated and newly-created VMs not communicating with VMs in other zones for a duration of up to 93 minutes. We apologize for the impact this event had on your applications and projects, and we will carefully investigate the causes and implement measures to prevent recurrences.
## DETAILED DESCRIPTION OF IMPACT:
On Sunday 18 January 2018, Google Compute Engine network provisioning updates failed in the following zones: 
europe-west3-a for 34 minutes (09:52 AM to 10:21 AM PT)
us-central1-b for 79 minutes (09:57 AM to 11:16 AM PT)
asia-northeast1-a for 93 minutes (09:53 AM to 11:26 AM PT)
Propagation of Google Compute Engine networking configuration for newly created and migrated VMs is handled by two components. The first is responsible for providing a complete list of VMâs, networks, firewall rules, and scaling decisions.  The second component provides a stream of updates for the components in a specific zone.
During the affected period, the first component failed to return data.  VMs in the affected zones were unable to communicate with newly-created or migrated VMs in another zone in the same private GCE network. VMs in the same zone were unaffected because they are updated by the streaming component.
The autoscaler service also relies upon data from the failed first component to scale instance groups; without updates from that component, it could not make scaling decisions for the affected zones.
## ROOT CAUSE:
A stuck process failed to provide updates to the Compute Engine control plane.  Automatic failover was unable to force-stop the process, and required manual failover to restore normal operation.
REMEDIATION AND PREVENTION
The engineering team was alerted when the propagation of network configuration information stalled.  They manually failed over to the replacement task to restore normal operation of the data persistence layer.
To prevent another occurrence of this incident, we are taking the following actions:
We still stop VM migrations if the configuration data is stale.
Modify the data persistence layer to re-resolve their peers during long-running processes, to allow failover to replacement tasks.

# [cloud/networking/18007](https://status.cloud.google.com/incident/cloud/networking/18007)
08:24 May 08, 2018
## ISSUE SUMMARY:
On Wednesday 2 May, 2018 Google Cloud Networking experienced increased packet loss to the internet as well as other Google regions from the us-central1 region for a duration of 21 minutes. We understand that the network is a critical component that binds all services together. We have conducted an internal investigation and are taking steps to improve our service.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 2 May, 2018 from 13:47 to 14:08 PDT, traffic between all zones in the us-central1 region and all destinations experienced 12% packet loss. Traffic between us-central1 zones experienced 22% packet loss. Customers may have seen requests succeed to services hosted in us-central1 as loss was not evenly distributed, some connections did not experience any loss while others experienced 100% packet loss.
## ROOT CAUSE:
A control plane is used to manage configuration changes to the network fabric connecting zones in us-central1 to each other as well as the Internet. On Wednesday 2 May, 2018 Google Cloud Network engineering began deploying a configuration change using the control plane as part of planned maintenance work. During the deployment, a bad configuration was generated that blackholed a portion of the traffic flowing over the fabric.
The control plane had a bug in it, which caused it to produce an incorrect configuration. New configurations deployed to the network fabric are evaluated for correctness, and regenerated if an error is found. In this case, the configuration error appeared after the configuration was evaluated, which resulted in deploying the erroneous configuration to the network fabric.
REMEDIATION AND PREVENTION
Automated monitoring alerted engineering teams 2 minutes after the loss started. Google engineers correlated the alerts to the configuration push and routed traffic away from the affected part of the fabric. Mitigation completed 21 minutes after loss began, ending impact to customers.
After isolating the root cause, engineers then audited all configuration changes that were generated by the control plane and replaced them with known-good configurations.
To prevent this from recurring, we will correct the control plane defect that generated the incorrect configuration and are adding additional validation at the fabric layer in order to more robustly detect configuration errors. Additionally, we intend on adding logic to the network control plane to be able to self-heal by automatically routing traffic away from the parts of the network fabric in an error state. Finally, we plan on evaluating further isolation of control plane configuration changes to reduce the size of the possible failure domain.
Again, we would like to apologize for this issue. We are taking immediate steps to improve the platformâs performance and availability.

# [cloud/networking/18009](https://status.cloud.google.com/incident/cloud/networking/18009)
13:32 May 22, 2018
## ISSUE SUMMARY:
On Wednesday 16 May 2018, Google Cloud Networking experienced loss of connectivity to external IP addresses located in us-east4 for a duration of 58 minutes.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 16 May 2018 from 18:43 to 19:41 PDT, Google Compute Engine, Google Cloud VPN, and Google Cloud Network Load Balancers hosted in the us-east4 region experienced 100% packet loss from the internet and other GCP regions. Google Dedicated Interconnect Attachments located in us-east4 also experienced loss of connectivity.
## ROOT CAUSE:
Every zone in Google Cloud Platform advertises several sets of IP addresses to the Internet via BGP.  Some of these IP addresses are global and are advertised from every zone, others are regional and advertised only from zones in the region. The software that controls the advertisement of these IP addresses contained a race condition during application startup that would cause regional IP addresses to be filtered out and withdrawn from a zone. During a routine binary rollout of this software, the race condition was triggered in each of the three zones in the us-east4 region. Traffic continued to be routed until the last zone received the rollout and stopped advertising regional prefixes. Once the last zone stopped advertising the regional IP addresses, external regional traffic stopped entering us-east4.
REMEDIATION AND PREVENTION
Google engineers were alerted to the problem within one minute and as soon as investigation pointed to a problem with the BGP advertisements, a rollback of the binary in the us-east4 region was created to mitigate the issue. Once the rollback proved effective, the original rollout was paused globally to prevent any further issues.
We are taking the following steps to prevent the issue from happening again. We are adding additional monitoring which will provide better context in future alerts to allow us to diagnose issues faster. We also plan on improving the debuggability of the software that controls the BGP advertisements. Additionally, we will be reviewing the rollout policy for these types of software changes so we can detect issues before they impact an entire region.
We apologize for this incident and we recognize that regional outages like this should be rare and quickly rectified. We are taking immediate steps to prevent recurrence and improve reliability in the future.

# [cloud/networking/18012](https://status.cloud.google.com/incident/cloud/networking/18012)
17:26 Jul 18, 2018
## ISSUE SUMMARY:
On Tuesday, 17 July 2018, customers using Google Cloud App Engine, Google HTTP(S) Load Balancer, or TCP/SSL Proxy Load Balancers experienced elevated error rates ranging between 33% and 87% for a duration of 32 minutes. Customers observed errors consisting of either 502 return codes, or connection resets. We apologize to our customers whose services or businesses were impacted during this incident, and we are taking immediate steps to improve the platformâs performance and availability. We will be providing customers with a SLA credit for the affected timeframe that impacted the Google Cloud HTTP(S) Load Balancer, TCP/SSL Proxy Load Balancer and Google App Engine products.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday, 17 July 2018, from 12:17 to 12:49 PDT, Google Cloud HTTP(S) Load Balancers returned 502s for some requests they received. The proportion of 502 return codes varied from 33% to 87% during the period. Automated monitoring alerted Googleâs engineering team to the event at 12:19, and at 12:44 the team had identified the probable root cause and deployed a fix. At 12:49 the fix became effective and the rate of 502s rapidly returned to a normal level. Services experienced degraded latency for several minutes longer as traffic returned and caches warmed. Serving fully recovered by 12:55. Connections to Cloud TCP/SSL Proxy Load Balancers would have been reset after connections to backends failed. Cloud services depending upon Cloud HTTP Load Balancing, such as Google App Engine application serving, Google Cloud Functions, Stackdriver's web UI, Dialogflow and the Cloud Support Portal/API, were affected for the duration of the incident.
Cloud CDN cache hits dropped 70% due to decreased references to Cloud CDN URLs from services behind Cloud HTTP(S) Load balancers and an inability to validate stale cache entries or insert new content on cache misses. Services running on Google Kubernetes Engine and using the Ingress resource would have served 502 return codes as mentioned above. Google Cloud Storage traffic served via Cloud Load Balancers was also impacted.
Other Google Cloud Platform services were not impacted. For example, applications and services that use direct VM access, or Network Load Balancing, were not affected.
## ROOT CAUSE:
Googleâs Global Load Balancers are based on a two-tiered architecture of Google Front Ends (GFE). The first tier of GFEs answer requests as close to the user as possible to maximize performance during connection setup. These GFEs route requests to a second layer of GFEs located close to the service which the request makes use of. This type of architecture allows clients to have low latency connections anywhere in the world, while taking advantage of Googleâs global network to serve requests to backends, regardless of in which region they are located.
The GFE development team was in the process of adding features to GFE to improve security and performance. These features had been introduced into the second layer GFE code base but not yet put into service. One of the features contained a bug which would cause the GFE to restart; this bug had not been detected in either of testing and initial rollout. At the beginning of the event, a configuration change in the production environment triggered the bug intermittently, which caused affected GFEs to repeatedly restart. Since restarts are not instantaneous, the available second layer GFE capacity was reduced. While some requests were correctly answered, other requests were interrupted (leading to connection resets) or denied due to a temporary lack of capacity while the GFEs were coming back online.
REMEDIATION AND PREVENTION
Google engineers were alerted to the issue within 3 minutes and began immediately investigating. At 12:44 PDT, the team discovered the root cause, the configuration change was promptly reverted, and the affected GFEs ceased their restarts. As all GFEs returned to service, traffic resumed its normal levels and behavior.
In addition to fixing the underlying cause, we will be implementing changes to both prevent and reduce the impact of this type of failure in several ways:
1. We are adding additional safeguards to disable features not yet in service.
2. We plan to increase hardening of the GFE testing stack to reduce the risk of having a latent bug in production binaries that may cause a task to restart.
3. We will also be pursuing additional isolation between different shards of GFE pools in order to reduce the scope of failures.
4. Finally, to speed diagnosis in the future, we plan to create a consolidated dashboard of all configuration changes for GFE pools, allowing engineers to more easily and quickly observe, correlate, and identify problematic changes to the system.
We would again like to apologize for the impact that this incident had on our customers and their businesses. We take any incident that affects the availability and reliability of our customers extremely seriously, particularly incidents which span regions. We are conducting a thorough investigation of the incident and will be making the changes which result from that investigation our very top priority in GCP engineering.

# [cloud/networking/18013](https://status.cloud.google.com/incident/cloud/networking/18013)
14:51 Aug 07, 2018
## ISSUE SUMMARY:
On Friday 27 July 2018, for a duration of 1 hour 4 minutes, Google Compute Engine (GCE) instances and Cloud VPN tunnels in europe-west4 experienced loss of connectivity to the Internet. The incident affected all new or recently live migrated GCE instances. VPN tunnels created during the incident were also impacted. We apologize to our customers whose services or businesses were impacted during this incident, and we are taking immediate steps to avoid a recurrence.
## DETAILED DESCRIPTION OF IMPACT:
All Google Compute Engine (GCE) instances in europe-west4 created on Friday 27 July 2018 from 18:27 to 19:31 PDT lost connectivity to the Internet and other instances via their public IP addresses. Additionally any instances that live migrated during the outage period would have lost connectivity for approximately 30 minutes after the live migration completed. All Cloud VPN tunnels created during the impact period, and less than 1% of existing tunnels in europe-west4 also lost external connectivity. All other instances and VPN tunnels continued to serve traffic. Inter-instance traffic via private IP addresses remained unaffected.
## ROOT CAUSE:
Google's datacenters utilize software load balancers known as Maglevs [1] to efficiently load balance network traffic [2] across service backends. The issue was caused by an unintended side effect of a configuration change made to jobs that are critical in coordinating the availability of Maglevs. The change unintentionally lowered the priority of these jobs in europe-west4. The issue was subsequently triggered when a datacenter maintenance event required load shedding of low priority jobs. This resulted in failure of a portion of the Maglev load balancers. However, a safeguard in the network control plane ensured that some Maglev capacity remained available. This layer of our typical defense-in-depth allowed connectivity to extant cloud resources to remain up, and restricted the disruption to new or migrated GCE instances and Cloud VPN tunnels.
REMEDIATION AND PREVENTION
Automated monitoring alerted Googleâs engineering team to the event within 5 minutes and they immediately began investigating at 18:36. At 19:25 the team discovered the root cause and started reverting the configuration change. The issue was mitigated at 19:31 when the fix was rolled out. At this point, connectivity was restored immediately.
In addition to addressing the root cause, we will be implementing changes to both prevent and reduce the impact of this type of failure by improving our alerting when too many Maglevs become unavailable, and adding a check for configuration changes to detect priority reductions on critical dependencies.
We would again like to apologize for the impact that this incident had on our customers and their businesses in the europe-west4 region. We are conducting a detailed post-mortem to ensure that all the root and contributing causes of this event are understood and addressed promptly.
[1] https://ai.google/research/pubs/pub44824
[2] https://cloudplatform.googleblog.com/2016/03/Google-shares-software-network-load-balancer-design-powering-GCP-networking.html

# [cloud/networking/18016](https://status.cloud.google.com/incident/cloud/networking/18016)
21:07 Oct 12, 2018
## ISSUE SUMMARY:
On Thursday 11 October 2018, a section of Google's network that includes part of us-central1-c lost connectivity to the Google network backbone that connects to the public internet for a duration of 41 minutes.
We apologize if your service or application was impacted by this incident. We are following our postmortem process to ensure we fully understand what caused this incident and to determine the exact steps we can take to prevent incidents of this type from recurring. Our engineering team is committed to prioritizing fixes for the most critical findings that result from our postmortem.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 11 October 2018 from 16:13 to 16:54 PDT, a section of Google's network that includes part of us-central1-c lost connectivity to the Google network backbone that connects to the public internet.
The us-central1-c zone is composed of two separate physical clusters. 61% of the VMs in us-central1-c were in the cluster impacted by this incident. Projects that create VMs in this zone have all of their VMs assigned to a single cluster. Customers with VMs in the zone were either impacted for all of their VMs in a project or for none.
Impacted VMs could not communicate with VMs outside us-central1 during the incident. VM-to-VM traffic using an internal IP address within us-central1 was not affected.
Traffic through the network load balancer was not able to reach impacted VMs in us-central1-c, but customers with VMs spread between multiple zones experienced the network load balancer shifting traffic to unaffected zones.
Traffic through the HTTP(S), SSL Proxy, and TCP proxy load balancers was not significantly impacted by this incident.
Other Google Cloud Platform services that experienced significant impact include the following:
30% of Cloud Bigtable clusters located in us-central1-c became unreachable.
10% of Cloud SQL instances in us-central lost external connectivity.
## ROOT CAUSE:
The incident occurred while Google's network operations team was replacing the routers that link us-central1-c to Google's backbone that connects to the public internet. Google engineers paused the router replacement process after determining that additional cabling would be required to complete the process and decided to start a rollback operation. The rollout and rollback operations utilized a version of workflow that was only compatible with the newer routers. Specifically, rollback was not supported on the older routers. When a configuration change was pushed to the older routers during the rollback, it deleted the Border Gateway Protocol (BGP) control plane sessions connecting the datacenter routers to the backbone routers resulting in a loss of external connectivity.
REMEDIATION AND PREVENTION
The BGP sessions were deleted in two tranches. The first deletion was at 15:43 and caused traffic to failover to other routers. The second set of BGP sessions were deleted at 16:13. The first alert for Google engineers fired at 16:16. We identified that the BGP sessions had been deleted at 16:41 and rolled back the configuration change at 16:52, ending the incident shortly thereafter.
The preventative action items identified so far include the following:
Fix the automated workflows for router replacements to ensure the correct version of workflows are utilized for both types of routers.
Alert when BGP sessions are deleted and traffic fails off, so that we can detect and mitigate problems before they impact customers.

# [cloud/networking/18019](https://status.cloud.google.com/incident/cloud/networking/18019)
14:49 Dec 21, 2018
## ISSUE SUMMARY:
On Wednesday 19 December 2018 multiple GCP services in europe-west1-b experienced a disruption for a duration of 34 minutes. Several GCP services were impacted: GCE, Monitoring, Cloud Console, GAE Admin API, Task Queues, Cloud Spanner, Cloud SQL, GKE, Cloud Bigtable, and Redis. GCP services in all other zones remained unaffected.
This service disruption was caused by an erroneous trigger leading to a switch re-installation during upgrades to two control plane network (CPN) switches impacting a portion of europe-west1-b. Most impacted GCP services in the zone recovered within a few minutes after the issue was mitigated.
We understand that these services are critical to our customers and sincerely apologize for the disruption caused by this incident. To prevent the issue from recurring we are fixing our repair workflows to catch such errors before serving traffic.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 19 December 2018 from 05:53 to 06:27 US/Pacific, multiple GCP services in europe-west1-b experienced disruption due to a network outage in one of Googleâs data centers.
The following Google Cloud Services in europe-west1-b were impacted: GCE instance creation, GCE networking, Cloud VPN, Cloud Interconnect,  Stackdriver Monitoring API, Cloud Console, App Engine Admin API, App Engine Task Queues, Cloud Spanner, Cloud SQL, GKE, Cloud Bigtable, and Cloud Memorystore for Redis. Most of these services suffered a brief disruption during the duration of the incident and recovered when the issue was mitigated.

Stackdriver: Around 1% of customers accessing Stackdriver Monitoring API directly received 5xx
errors.
Cloud Console: Affected customers may not have been able to view graphs and API usage
statistics. Impacted dashboards include: /apis/dashboard, /home/dashboard, /google/maps-api/api 
list.             
Redis: After the network outage ended, ~50 standard Redis instances in europe-west1 remained
unavailable until 07:55 US/Pacific due to a failover bug triggered by the outage. 

## ROOT CAUSE:
As part of a program to upgrade network switches in control plane networks across Googleâs data center, two control plane network (CPN) switches supporting a single CPN were scheduled to undergo upgrades. On December 17, the first switch was upgraded and was back online the same day. The issue triggered on December 19 when the second switch was due to be upgraded. During the upgrade of the second switch, a reinstallation was erroneously triggered on the first switch, causing it to go offline for a short period of time. Having both switches down partitioned the network supporting a portion of europe-west1-b. Due to this isolation, the zone was left partially functional.
REMEDIATION AND PREVENTION
The issue was mitigated at 06:27 US/Pacific when reinstallation of the first switch in the CPN completed.
To prevent the issue from recurring we are changing the switch upgrade workflow to prevent erroneous triggers. The trigger inadvertently caused the switch to re-install before any CPN switch is deemed healthy to serve traffic. We are also adding additional checks to make sure upgraded devices are in full functional state before they are deemed healthy to start serving. We will also be improving our automation to catch offline peer devices sooner and help prevent related issues.

# [cloud/networking/19005](https://status.cloud.google.com/incident/cloud/networking/19005)
13:43 Mar 12, 2019
## ISSUE SUMMARY:
On Wednesday 6 March 2019, Google Cloud Router and Cloud Interconnect experienced a service disruption in the us-east4 region for a duration of 8 hours and 34 minutes. Cloud VPN configurations with dynamic routes via Cloud Router were impacted during this time. We apologize to our customers who were impacted by this outage.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 6 March 2019 from 20:17 to Thursday 7 March 04:51 US/Pacific, Cloud Router and Cloud Interconnect experienced a service disruption in us-east4. Customers utilizing us-east4 were unable to advertise routes to their Google Compute Engine (GCE) instances or learn routes from GCE.
Cloud VPN traffic with dynamic routes over Cloud Router and Cloud Interconnect in us-east4 was impacted by this service disruption. Cloud VPN traffic over pre-configured static routes was unaffected and continued to function without disruption during this time.
## ROOT CAUSE:
The Cloud Router control plane service assigns Cloud Router tasks to individual customers and creates routes between those tasks and customer VPCs. Individual Cloud Router tasks establish external BGP sessions and propagate routes to and from the control plane service.
A disruption occurred during the rollout of a new version of the control plane service in us-east4. This required the control plane to restart from a âcoldâ state requiring it to validate all assignments of the Cloud Router tasks. The control plane service did not successfully initialize and it was unable to assign individual Cloud Router tasks in order to propagate routes between those tasks and customer VPCs. Cloud Router tasks became temporarily disassociated with customers and BGP sessions were terminated. As a result, Cloud VPN and Cloud Interconnect configurations that were dependent on Cloud Router in us-east4 were unavailable during this time.
REMEDIATION AND PREVENTION
Google engineers were automatically alerted at 20:30 PST on 6 March 2019 and immediately began an investigation. A fix for the control plane service was tested, integrated, and rolled out on 7 March 2019 at 04:33 US/Pacific. The control plane service fully recovered by 05:16 US/Pacific.
We are taking immediate steps to prevent recurrence. The issue that prevented the control plane from restarting has been resolved. In order to ensure faster incident detection, we are improving control plane service testing, the instrumentation of Cloud Router tasks, and the control plane service instrumentation.

# [cloud/networking/19007](https://status.cloud.google.com/incident/cloud/networking/19007)
18:10 Apr 10, 2019
## ISSUE SUMMARY:
On Thursday 4 April 2019, Cloud VPN  configurations with dynamic routes via Cloud Router, Cloud Dedicated Interconnect attachments, and Cloud Partner Interconnect attachments in us-central1 experienced a service disruption for a duration of 70 minutes.  We apologize to all our customers who were impacted by the incident.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 4 April 2019, from 15:40 to 16:50 US/Pacific, Google Cloud Routers and Cloud Interconnect experienced a service disruption in us-central1. Cloud Routers for Cloud Interconnect and Cloud VPN were unable to route traffic in us-central1 for the duration of the incident. This impacted Cloud Private Interconnect attachments and Cloud VPN tunnels using dynamic routing. Global routing and Cloud VPN tunnels utilizing static routes were not affected during the incident.
## ROOT CAUSE:
The Cloud Router control plane service assigns Cloud Router tasks to individual customers and creates routes between those tasks and customer VPCs. Individual Cloud Router tasks connected to the control plane service are responsible for establishing external BGP sessions and propagating routes to and from the service.
The disruption was caused by a rollout to the Cloud Router control plane service. One part of the control plane rollout process changed the version of the service which cloud router tasks connect to, performed through a leader election process. When the new version was elected leader, cloud router tasks encountered an issue while disassociating with the previous leader. This issue caused tasks to stay connected to the previous leader for an extended duration. The delay resulted in individual cloud router tasks losing state, requiring the system to be initialized from a âcoldâ state.
Changes in the new version allowed the system to complete initialization without any intervention. During initialization, cloud router tasks were reassigned to customers and started to re-establish sessions. Until all customersâ tasks were reassigned, routes learned from these Cloud Routers were not propagated and services dependent on Cloud Routers remained impacted in us-central1.
REMEDIATION AND PREVENTION
Google engineers were alerted to the disruption at 15:41 US/Pacific on 4 April 2019 and began to investigate immediately. Once the root cause was determined, the rollout was paused and control plane tasks running the previous version were canceled to ensure that the previous version would not be elected leader. The leader task was then restarted to ensure that all cloud router tasks connected to the service running the new version. The service then recovered.
The actions we took, based on previous learnings,  greatly reduced the duration of this disruption; however, to further reduce and prevent recurrence, we are changing the logic in both the control plane service and cloud router tasks to ensure that when there is a leadership change, cloud router tasks connect to the new leader quickly and keep their state.
Should a âcoldâ state initialization reoccur, we are optimizing the initialization logic to finish more quickly, reducing recovery time for this type of incident. Furthermore, we will review control planes across Google Cloud Platform and analyze how the systems perform under a âcoldâ start scenario to ensure they meet customer requirements.

# [cloud/networking/19009](https://status.cloud.google.com/incident/cloud/networking/19009)
09:42 Jun 06, 2019
## ISSUE SUMMARY:
On Sunday 2 June, 2019, Google Cloud projects running services in multiple US regions experienced elevated packet loss as a result of network congestion for a duration of between 3 hours 19 minutes, and 4 hours 25 minutes. The duration and degree of packet loss varied considerably from region to region and is explained in detail below. Other Google Cloud services which depend on Google's US network were also impacted, as were several non-Cloud Google services which could not fully redirect users to unaffected regions. Customers may have experienced increased latency, intermittent errors, and connectivity loss to instances in us-central1, us-east1, us-east4, us-west2, northamerica-northeast1, and southamerica-east1. Google Cloud instances in us-west1, and all European regions and Asian regions, did not experience regional network congestion.
Google Cloud Platform services were affected until mitigation completed for each region, including: Google Compute Engine, App Engine, Cloud Endpoints, Cloud Interconnect, Cloud VPN, Cloud Console, Stackdriver Metrics, Cloud Pub/Sub, Bigquery, regional Cloud Spanner instances, and Cloud Storage regional buckets. G Suite services in these regions were also affected.
We apologize to our customers whose services or businesses were impacted during this incident, and we are taking immediate steps to improve the platformâs performance and availability. A detailed assessment of impact is at the end of this report.
ROOT CAUSE AND REMEDIATION
This was a major outage, both in its scope and duration. As is always the case in such instances, multiple failures combined to amplify the impact.
Within any single physical datacenter location, Google's machines are segregated into multiple logical clusters which have their own dedicated cluster management software, providing resilience to failure of any individual cluster manager. Google's network control plane runs under the control of different instances of the same cluster management software; in any single location, again, multiple instances of that cluster management software are used, so that failure of any individual instance has no impact on network capacity.
Google's cluster management software plays a significant role in automating datacenter maintenance events, like power infrastructure changes or network augmentation. Google's scale means that maintenance events are globally common, although rare in any single location. Jobs run by the cluster management software are labelled with an indication of how they should behave in the face of such an event: typically jobs are either moved to a machine which is not under maintenance, or stopped and rescheduled after the event.
Two normally-benign misconfigurations, and a specific software bug, combined to initiate the outage: firstly, network control plane jobs and their supporting infrastructure in the impacted regions were configured to be stopped in the face of a maintenance event. Secondly, the multiple instances of cluster management software running the network control plane were marked as eligible for inclusion in a particular, relatively rare maintenance event type. Thirdly, the software initiating maintenance events had a specific bug, allowing it to deschedule multiple independent software clusters at once, crucially even if those clusters were in different physical locations.
The outage progressed as follows: at 11:45 US/Pacific, the previously-mentioned maintenance event started in a single physical location; the automation software created a list of jobs to deschedule in that physical location, which included the logical clusters running network control jobs. Those logical clusters also included network control jobs in other physical locations. The automation then descheduled each in-scope logical cluster, including the network control jobs and their supporting infrastructure in multiple physical locations.
Google's resilience strategy relies on the principle of defense in depth. Specifically, despite the network control infrastructure being designed to be highly resilient, the network is designed to 'fail static' and run for a period of time without the control plane being present as an additional line of defense against failure. The network ran normally for a short period - several minutes - after the control plane had been descheduled. After this period, BGP routing between specific impacted physical locations was withdrawn, resulting in the significant reduction in network capacity observed by our services and users, and the inaccessibility of some Google Cloud regions. End-user impact began to be seen in the period 11:47-11:49 US/Pacific.
Google engineers were alerted to the failure two minutes after it began, and rapidly engaged the incident management protocols used for the most significant of production incidents. Debugging the problem was significantly hampered by failure of tools competing over use of the now-congested network. The defense in depth philosophy means we have robust backup plans for handling failure of such tools, but use of these backup plans (including engineers travelling to secure facilities designed to withstand the most catastrophic failures, and a reduction in priority of less critical network traffic classes to reduce congestion) added to the time spent debugging. Furthermore, the scope and scale of the outage, and collateral damage to tooling as a result of network congestion, made it initially difficult to precisely identify impact and communicate accurately with customers.
As of 13:01 US/Pacific, the incident had been root-caused, and engineers halted the automation software responsible for the maintenance event. We then set about re-enabling the network control plane and its supporting infrastructure. Additional problems once again extended the recovery time: with all instances of the network control plane descheduled in several locations, configuration data had been lost and needed to be rebuilt and redistributed. Doing this during such a significant network configuration event, for multiple locations, proved to be time-consuming. The new configuration began to roll out at 14:03.
In parallel with these efforts, multiple teams within Google applied mitigations specific to their services, directing traffic away from the affected regions to allow continued serving from elsewhere.
As the network control plane was rescheduled in each location, and the relevant configuration was recreated and distributed, network capacity began to come back online. Recovery of network capacity started at 15:19, and full service was resumed at 16:10 US/Pacific time.
The multiple concurrent failures which contributed to the initiation of the outage, and the prolonged duration, are the focus of a significant post-mortem process at Google which is designed to eliminate not just these specific issues, but the entire class of similar problems. Full details follow in the Prevention and Follow-Up section.
PREVENTION AND FOLLOW-UP
We have immediately halted the datacenter automation software which deschedules jobs in the face of maintenance events. We will re-enable this software only when we have ensured the appropriate safeguards are in place to avoid descheduling of jobs in multiple physical locations concurrently. Further, we will harden Google's cluster management software such that it rejects such requests regardless of origin, providing an additional layer of defense in depth and eliminating other similar classes of failure.
Google's network control plane software and supporting infrastructure will be reconfigured such that it handles datacenter maintenance events correctly, by rejecting maintenance requests of the type implicated in this incident. Furthermore, the network control plane in any single location will be modified to persist its configuration so that the configuration does not need to be rebuilt and redistributed in the event of all jobs being descheduled. This will reduce recovery time by an order of magnitude. Finally, Google's network will be updated to continue in 'fail static' mode for a longer period in the event of loss of the control plane, to allow an adequate window for recovery with no user impact.
Google's emergency response tooling and procedures will be reviewed, updated and tested to ensure that they are robust to network failures of this kind, including our tooling for communicating with the customer base. Furthermore, we will extend our continuous disaster recovery testing regime to include this and other similarly catastrophic failures.
Our post-mortem process will be thorough and broad, and remains at a relatively early stage. Further action items may be identified as this process progresses.
## DETAILED DESCRIPTION OF IMPACT:
Compute Engine
Compute Engine instances in us-east4, us-west2, northamerica-northeast1 and southamerica-east1 were inaccessible for the duration of the incident, with recovery times as described above.
Instance to instance packet loss for traffic on private IPs and internet traffic:

us-east1 up to 33% packet loss from 11:38 to 12:17, up to 8% packet loss from 12:17 to 14:50.
us-central1 spike of 9% packet loss immediately after 11:38 and subsiding by 12:05.
us-west1 initial spikes up to 20% and 8.6% packet loss to us-east1 and us-central1 respectively, falling below 0.1% by 12:55. us-west1 to European regions saw an initial packet loss of up to 1.9%, with packet loss subsiding by 12:05. us-west1 to Asian regions did not see elevated packet loss.

Instances accessing Google services via Google Private Access were largely unaffected.
Compute Engine admin operations returned an average of 1.2% errors.
App Engine
App Engine applications hosted in us-east4, us-west2, northamerica-northeast1 and southamerica-east1 were unavailable for the duration of the disruption. The us-central region saw a 23.2% drop in requests per second (RPS). Requests that reached App Engine executed normally, while requests that did not returned client timeout errors.
Cloud Endpoints
Requests to Endpoints services during the network incident experienced a spike in error rates up to 4.4% at the start of the incident, decreasing to 0.6% average error rate between 12:50 and 15:40, at 15:40 error rates decreased to less than 0.1%. A separate Endpoints incident was caused by this disruption and its impact extended beyond the resolution time above.
From Sunday 2 June, 2019 12:00 until Tuesday 4 June, 2019 11:30, 50% of service configuration push workflows failed. For the duration of the Cloud Endpoints disruption, requests to existing Endpoints services continued to serve based on an existing configuration. Requests to new Endpoints services, created after the disruption start time, failed with 500 errors unless the ESP flag service_control_network_fail_open was enabled, which is disabled by default.
Since Tuesday 4 June, 2019 11:30, service configuration pushes have been successful, but may take up to one hour to take effect. As a result, requests to new Endpoints services may return 500 errors for up to 1 hour after the configuration push. We expect to return to the expected sub-minute configuration propagation by Friday 7 June 2019. Customers who are running on platforms other than Google App Engine Flex can work around this by setting the ESP flag service_control_network_fail_open to true. For customers whose backend is running on Google App Engine Flex, there is no mitigation for the delayed config pushes available at this time.
Cloud Interconnect
Cloud Interconnect reported packet loss ranging from 10% to 100% in affected regions during this incident. Interconnect Attachments in us-east4, us-west2, northamerica-northeast1 and southamerica-east1 reported packet loss ranging from 50% to 100% from 11:45 to 16:10. As part of this packet loss, some BGP sessions also reported going down. During this time, monitoring statistics were inconsistent where the disruption impacted our monitoring as well as Stackdriver monitoring, noted below. As a result we currently estimate that us-east4, us-west2, northamerica-northeast1 and southamerica-east1 sustained heavy packet loss until recovery at approximately 16:10. Further, Interconnect Attachments located in us-west1, us-east1, and us-central1 but connecting from Interconnects located on the east coast (e.g. New York, Washington DC) saw 10-50% packet loss caused by congestion on Googleâs backbone in those geographies during this same time frame.
Cloud VPN
Cloud VPN gateways in us-east4, us-west2, northamerica-northeast1 and southamerica-east1 were unreachable for the duration of the incident. us-central1 VPN endpoints reported 25% packet loss and us-east1 endpoints reported 10% packet loss. VPN gateways in us-east4 recovered at 15:40. VPN gateways in us-west2, northamerica-northeast1 and southamerica-east1 recovered at 16:30. Additional intervention was required in us-west2, northamerica-northeast1 and southamerica-east1 to move the VPN control plane in these regions out of a fail-safe state, designed to protect existing gateways from potentially incorrect changes, caused by the disruption.
Cloud Console
Cloud Console customers may have seen pages load more slowly, partially or not at all. Impact was more severe for customers who were in the eastern US as the congested links were concentrated between central US and eastern US regions for the duration of the disruption.
Stackdriver Monitoring
Stackdriver Monitoring experienced a 5-10% drop in requests per second (RPS) for the duration of the event. Login failures to the Stackdriver Monitoring Frontend averaged 8.4% over the duration of the incident. The frontend was also loading with increased latency and encountering a 3.5% error rate when loading data in UI components.
Cloud Pub/Sub
Cloud Pub/Sub experienced Publish and Subscribe unavailability in the affected regions averaged over the duration of the incident:

us-east4 publish requests reported 0.3% error rate and subscribe requests reported a 25% error rate.
southamerica-east1 publish requests reported 11% error rate and subscribe requests reported a 36% error rate.
northamerica-northeast1 publish requests reported a 6% error rate and subscribe requests reported a 31% error rate.
us-west2 did not have a statistically significant change in usage.

Additional Subscribe unavailability was experienced in other regions on requests for messages stored in the affected Cloud regions. Analysis shows a 27% global drop in successful publish and subscribe requests during the disruption. There were two periods of global unavailability for Cloud Pub/Sub Admin operations (create/delete topic/subscriptions) . First from 11:50 to 12:05 and finally from 16:05 to 16:25.
BigQuery
BigQuery saw an average error rate of 0.7% over the duration of the incident. Impact was greatest at the beginning of the incident, between 11:47 and 12:02 where jobs.insert API calls had an error rate of 27%. Streaming Inserts (tabledata.insertAll API calls) had an average error rate of less than 0.01% over the duration of the incident, peaking to 24% briefly between 11:47 and 12:02.
Cloud Spanner
Cloud Spanner in regions us-east4, us-west2, and northamerica-northeast1 were unavailable during the duration 11:48 to 15:44. We are continuing to investigate reports that multi-region nam3 was affected, as it involves impacted regions. Other regions' availability was not affected. Modest latency increases at the 50th percentile were observed in us-central1 and us-east1 regions for brief periods during the incident window; exact values were dependent on customer workload. Significant latency increases at the 99th percentile were observed:

nam-eur-asia1 had 120 ms of additional latency from 13:50 to 15:20.
nam3 had greater than 1 second of additional latency from 11:50 to 13:10, from 13:10 to 16:50 latency was increased by 100 ms.
nam6 had an additional 320 ms of latency between 11:50 to 13:10, from 13:10 to 16:50 latency was increased by 130 ms.
us-central1 had an additional 80 ms of latency between 11:50 to 13:10, from 13:10 to 16:50 latency was increased by 10 ms.
us-east1 had an additional 2 seconds of latency between 11:50 to 13:10, from 13:10 to 15:50 latency was increased by 250 ms.
us-west1 had an additional 20 ms of latency between 11:50 to 14:10.

Cloud Storage
Cloud Storage average error rates for bucket locations during the incident are as follows. This data is the best available approximation of the error rate available at the time of publishing:

us-west2 96.2%
southamerica-east1 79.3%
us-east4 62.4%
northamerica-northeast1 43.4%
us 3.5%
us-east1 1.7%
us-west1 1.2%
us-central1 0.7%

G Suite
The impact on G Suite users was different from and generally lower than the impact on Google Cloud users due to differences in architecture and provisioning of these services. Please see the G Suite Status Dashboard (https://www.google.com/appsstatus) for details on affected G Suite services.
SLA CREDITS
If you believe your paid application experienced an SLA violation as a result of this incident, please populate the SLA credit request: https://support.google.com/cloud/contact/cloud_platform_sla
A full list of all Google Cloud Platform Service Level Agreements can be found at https://cloud.google.com/terms/sla/.
For G Suite, please request an SLA credit through one of the Support channels: https://support.google.com/a/answer/104721
G Suite Service Level Agreement can be found at https://gsuite.google.com/intl/en/terms/sla.html

# [cloud/pubsub/16003](https://status.cloud.google.com/incident/cloud/pubsub/16003)
21:42 Nov 03, 2016
## SUMMARY:
On Monday, 31 October 2016, 73% of requests to create new subscriptions for Google Cloud Pub/Sub failed for a duration of 124 minutes. Creation of new Cloud SQL Second Generation instances also failed during this incident.
If your service or application was affected, we apologize. We have conducted a detailed review of the causes of this incident and are ensuring that we apply the appropriate fixes so that it will not recur.
## DETAILED DESCRIPTION OF IMPACT:
On Monday, 31 October 2016 from 13:11 to 15:15 PDT, 73% of requests to create new subscriptions for Google Cloud Pub/Sub failed.
0.1% of pull requests experienced latencies of up to 4 minutes for end-to-end message delivery.
Creation of all new Cloud SQL Second Generation instances also failed during this incident. Existing instances were not affected.
## ROOT CAUSE:
At 13:08, a system in the Cloud Pub/Sub control plane experienced a connectivity issue to its persistent storage layer for a duration of 83 seconds. This caused a queue of storage requests to build up. When the storage layer re-connected, the queued requests were executed, which exceeded the available processing quota for the storage system. The system entered a feedback loop in which storage requests continued to queue up leading to further latency increases and more queued requests. The system was unable to exit from this state until additional capacity was added.
Creation of a new Cloud SQL Second Generation instance requires a new Cloud Pub/Sub subscription.
REMEDIATION AND PREVENTION:
Our monitoring systems detected the outage and paged oncall engineers at 13:19. We determined root cause at 14:05 and acquired additional storage capacity for the Pub/Sub control plane at 14:42. The outage ended at 15:15 when this capacity became available.
To prevent this issue from recurring, we have already increased the storage capacity for the Cloud Pub/Sub control plane. We will change the retry behavior of the control plane to prevent a feedback loop if storage quota is temporarily exceeded. We will also improve our monitoring to ensure we can determine root cause for this type of failure more quickly in future.
We apologize for the inconvenience this issue caused our customers.

# [cloud/pubsub/17001](https://status.cloud.google.com/incident/cloud/pubsub/17001)
22:19 Mar 29, 2017
## ISSUE SUMMARY:
On Tuesday 21 March 2017, new connections to Cloud Pub/Sub experienced high latency leading to timeouts and elevated error rates for a duration of 95 minutes. Connections established before the start of this issue were not affected. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 21 March 2017 from 21:08 to 22:43 US/Pacific, Cloud Pub/Sub publish, pull and ack methods experienced elevated latency, leading to timeouts. The average error rate for the issue duration was 0.66%. The highest error rate occurred at 21:43, when the Pub/Sub publish error rate peaked at 4.1%, the ack error rate reached 5.7% and the pull error rate was 0.02%.
## ROOT CAUSE:
The issue was caused by the rollout of a storage system used by the Pub/Sub service.  As part of this rollout, some servers were taken out of service, and as planned, their load was redirected to remaining servers.  However, an unexpected imbalance in key distribution led some of the remaining servers to become overloaded. The Pub/Sub service was then unable to retrieve the status required to route new connections for the affected methods. Additionally, some Pub/Sub servers didnât recover promptly after the storage system had been stabilized and required individual restarts to fully recover.
REMEDIATION AND PREVENTION
Google engineers were alerted by automated monitoring seven minutes after initial impact.  At 21:24, they had correlated the issue with the storage system rollout and stopped it from proceeding further.  At 21:41, engineers restarted some of the storage servers, which improved systemic availability. Observed latencies for Pub/Sub were still elevated, so at 21:54, engineers commenced restarting other Pub/Sub servers, restoring service to 90% of users. At 22:29 a final batch was restarted, restoring the Pub/Sub service to all.
To prevent a recurrence of the issue, Google engineers are creating safeguards to limit the number of keys managed by each server. They are also improving the availability of Pub/Sub servers to respond to requests even when in an unhealthy state. Finally they are deploying enhancements to the Pub/Sub service to operate when the storage system is unavailable.

# [cloud/pubsub/19001](https://status.cloud.google.com/incident/cloud/pubsub/19001)
13:13 May 28, 2019
## ISSUE SUMMARY:
On Monday 20 May, 2019, Google Cloud Pub/Sub experienced publish error rates of 1.2%, increased publish latency by 1.7ms at the 50th percentile, and 8.3s increase at the 99th percentile for a duration of 3 hours, 30 minutes. Publish and Subscribe admin operations saw average error rates of 8.3% and 3.2% respectively for the same period. We apologize to our customers who were impacted by this service degradation.
## DETAILED DESCRIPTION OF IMPACT:
On Monday 20 May, 2019 from 20:54 to Tuesday 21 May, 2019 00:24 US/Pacific Google Cloud Pub/Sub experienced publish error rates of 1.2%, increased publish latency by 1.7ms at the 50th percentile, and 8.3s increase at the 99th percentile for a duration of 3 hours, 30 minutes. Publish (CreateTopic, GetTopic, UpdateTopic, DeleteTopic) and Subscribe (CreateSnapshot, CreateSubscription, UpdateSubscription) admin operations saw average error rates of 8.3% and 3.2% respectively for the same period. Customers affected by the incident may have seen errors containing messages like âDEADLINE_EXCEEDEDâ.
Cloud Pub/Subâs elevated error rates and increased latency indirectly impacted Cloud SQL, Cloud Filestore, and App Engine Task Queues globally. The incident caused elevated error rates in admin operations (including instance creation) for both Cloud SQL and Cloud Filestore, as well as increased latencies and timeout errors for App Engine Task Queues during the incident.
## ROOT CAUSE:
The incident was triggered by an internal user creating an unexpected surge of publish requests to Cloud Pub/Sub topics. These requests did not cache as expected and led to hotspotting on the underlying metadata storage system responsible for managing Cloud Pub/Subâs publish and subscribe operations. The hotspotting triggered overload protection mechanisms within the storage system which began to reject some incoming requests and delay the processing of others, both of which contributed to the elevated error rates and increased latencies experienced by Cloud Pub/Sub.
REMEDIATION AND PREVENTION
On Monday 20 May, 2019 at 21:16 US/Pacific Google engineers were automatically alerted to elevated error rates and immediately began their investigation. At 22:18, we determined the underlying storage system was responsible for the elevated error rates afflicting Cloud Pub/Sub and escalated the issue to the storage systemâs engineering team. At 22:48, Google engineers attempted to mitigate the issue by providing additional resources to the impacted storage system servers, however, this did not address the hotspots and error rates remained elevated. At 23:00, Google engineers disabled non-essential internal traffic to reduce load being sent to the storage system, this improved system behavior, but did not lead to a full recovery. On Tuesday 21 May, 2019 at 00:19 US/Pacific, Google engineers identified the source for the surge of requests and implemented a rate limit on the requests, which effectively mitigated the issue. Once the traffic had subsided, the storage systemâs automated mechanisms were able to successfully heal the service, leading to full resolution of the incident by 00:24.
In order to prevent a recurrence of the incident we are adding an additional layer of caching to further reduce load on the metadata storage system. We are preemptively increasing the number of storage servers to improve isolation, improve load distribution, and reduce the effect hotspotting may have. We are reviewing the schema of the storage system to improve load distribution. Finally we will be improving our playbooks with learnings from this incident, specifically improving sections around rate limiting, load shedding and hotspot detection.

# [cloud/sql/17004](https://status.cloud.google.com/incident/cloud/sql/17004)
22:04 Nov 18, 2014
## SUMMARY:
On Tuesday 18 November, 2.2% of Cloud SQL instances hosted in European datacenters were unavailable for a duration of 18 minutes. We apologize if your instance was affected. We will be taking steps to improve the serviceâs availability as a result of this incident.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 18 November from 06:32 to 06:50 PST, any Cloud SQL instance hosted in a European datacenterrestarted after attempting a write operation. Users trying to connect to affected instances during the incident received connection errors.
## ROOT CAUSE:
A networking issue caused elevated packet loss to one European datacenter. Cloud SQL instances that attempted to replicate data to this datacenter restarted, causing them to become unavailable for the duration of the incident.
REMEDIATION AND PREVENTION:
Googleâs network engineers detected the problem immediately after it occurred at 06:32. We implemented a fix for the networking problem at 06:48 and the packet loss stopped at 06:50.
We will make changes to Cloud SQL to ensure that unavailability of a single datacenter in Europe does not cause instances to restart.

# [cloud/sql/17005](https://status.cloud.google.com/incident/cloud/sql/17005)
06:01 Jan 22, 2015
## SUMMARY:
On Tuesday 20 January 2015, for a duration of 103 minutes, Google Compute Engine experienced an issue with outbound network connectivity to certain IP blocks which were used for other Google services. Compute Engine instances were not able to connect to IPs in the affected blocks, meaning that other Google services, including Cloud SQL and BigQuery, were unavailable to some Compute Engine users. We apologize for this disruption in connectivity, and are taking immediate steps to prevent its recurrence.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 20 January 2015 from 17:27 to 19:10 PST, the Google Compute Engine routing layer dropped connections to 33% of Google IP blocks. Compute Engine instances were impacted if they attempted to connect to a Google service (including Cloud SQL and BigQuery) and were given an IP in one of the affected blocks by Google DNS servers. 21% of GCE instances, distributed across all Compute Engine zones, attempted connections to the affected blocks during the incident.
## ROOT CAUSE:
At 17:27 a configuration change previously initiated by Google engineers was rolled out to Google Compute Engine routers by an automated system. This change was intended to disable routing traffic to certain IP blocks, but due to a manual misconfiguration, the configured netblocks were too large, and included addresses used by Google services in production. Due to an unrelated process error, this configuration change was rolled out to the Compute Engine routing system before automated tests were run. Once the changes were rolled out, any traffic from a Compute Engine instance destined to Google services in the incorrectly labelled blocks would be erroneously dropped.
REMEDIATION AND PREVENTION:
Automated network monitoring systems alerted Google engineers of the issue at 17:31. Google engineers identified incorrectly labeled netblocks as the root cause at 18:35, and began deploying a fix at 18:58. As the labels were corrected by the fix, the system began to recover; full recovery was complete at 19:10.
Google engineers are correcting the process used to push this network configuration to the Compute Engine routing system to utilize the existing automated tests. Additionally, the process to label netblocks will now include peer review, and the tool used to generate these changes is being improved to reduce the risk of errors. Finally, Google engineers are revising the process by which changes are rolled out to Compute Engine routing infrastructure to ensure changes are rolled out gradually across all zones.

# [cloud/sql/17008](https://status.cloud.google.com/incident/cloud/sql/17008)
18:54 Jul 15, 2015
## SUMMARY:
On Friday, June 26 2015 13:04 PDT, connections to Cloud SQL instances in one datacenter in the United States failed for a duration of 19 minutes. We apologise if you were affected by this issue. Our engineers have completed a postmortem analysis of this incident and are performing remediation tasks to prevent similar issues in the future.
## DETAILED DESCRIPTION OF IMPACT:
On Friday, June 26 2015 from 13:04 to 13:23 PDT, traffic to affected Cloud SQL instances in United States was impacted. Existing connections were dropped and new connections could not be established. Approximately 4% of Cloud SQL instances in the United States also were also rebooted.
## ROOT CAUSE:
A manual procedure to reprogram the power supply of a router as part of a maintenance routine didnât have the desired effect and caused the router to restart in an undesired manner. The team performing the routine detected the issue immediately and was able to restore the system to a stable state within 20 minutes.
REMEDIATION AND PREVENTION:
We have identified areas of improvement needed to prevent similar issues in the future. We have taken measures to prevent issues with the same root cause to reappear in the future. We are also adding additional monitoring metrics to alert for failures at this level earlier and improve cross-team communication for planned maintenance events.

# [cloud/sql/17009](https://status.cloud.google.com/incident/cloud/sql/17009)
02:26 Aug 18, 2015
## SUMMARY:
On Friday, 14 August 2015, Google Cloud SQL instances in the US Central region experienced intermittent connectivity issues over an interval of 6 hours 50 minutes. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Friday, 14 August 2015 from 03:24 to 10:16 PDT, some attempts to connect to Google Cloud SQL instances in the US Central region failed.  Approximately 12% of all active Cloud SQL instances experienced a denied connection attempt.
## ROOT CAUSE:
On Wednesday, 12 August 2015, a standard rollout was performed for Google Cloud SQL which introduced a memory leak in the serving component.  Before the rollout, an unrelated periodic maintenance activity necessitated disabling some automated alerts, and these were not enabled again once maintenance was complete.  As a result, Google engineers were not alerted to high resource usage until Cloud SQL serving tasks began exceeding resource limits and rejecting more incoming connections.
REMEDIATION AND PREVENTION:
At 07:47, Google engineers were alerted to high reported error rates and began allocating more resources for Cloud SQL serving tasks, which provided an initial reduction in error rates.  Finally, a restart of running Cloud SQL serving tasks eliminated remaining connectivity issues by 10:16.
To prevent the issue from recurring, we are implementing mitigation and monitoring changes as a result of this incident, which include rolling back the problematic update, making the Cloud SQL serving component more resilient to high resource usage, and improving monitoring procedures to reduce the time taken to detect and isolate similar problems.

# [cloud/sql/17010](https://status.cloud.google.com/incident/cloud/sql/17010)
11:09 May 20, 2016
## SUMMARY:
On Tuesday 17 May 2016, connections to Cloud SQL instances in the Central United States region experienced an elevated error rate for 130 minutes.
We apologize to customers who were affected by this incident. We know that reliability is critical for you and we are committed to learning from incidents in order to improve the future reliability of our service.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 17 May 2016 from 04:15 to 06:12 and from 08:24 to 08:37 PDT, connections to Cloud SQL instances in the us-central1 region experienced an elevated error rate. The average rate of connection errors to instances in this region was 10.5% during the first part of the incident and 1.9% during the second part of the incident. 51% of in-use Cloud SQL instances in the affected region were impacted during the first part of the incident; 4.2% of in-use instances were impacted during the second part. Cloud SQL Second Generation instances were not impacted.
## ROOT CAUSE:
Clients connect to a Cloud SQL frontend service that forwards the connection to the correct MySQL database server. The frontend calls a separate service to start up a new Cloud SQL instance if a connection arrives for an instance that is not running.
This incident was triggered by a Cloud SQL instance that could not successfully start. The incoming connection requests for this instance resulted in a large number of calls to the start up service. This caused increased memory usage of the frontend service as start up requests backed up. The frontend service eventually failed under load and dropped some connection requests due to this memory pressure.
REMEDIATION AND PREVENTION:
Google received its first customer report at 04:39 PDT and we tried to remediate the problem by redirecting new connections to different datacenters. This effort proved unsuccessful as the start up capacity was used up there also. At 06:12 PDT, we fixed the issue by blocking all incoming connections to the misbehaving Cloud SQL instance. At 08:24 PDT, we moved this instance to a separate pool of servers and restarted it. However, the separate pool of servers did not provide sufficient isolation for the service that starts up instances, causing the incident to recur. We shutdown the instance at 08:37 PDT which resolved the incident.
To prevent incidents of this type in the future, we will ensure that a single Cloud SQL instance cannot use up all the capacity of the start up service.
In addition, we will improve our monitoring in order to detect this type of issue more quickly.
We apologize for the inconvenience this issue caused our customers.

# [cloud/sql/17012](https://status.cloud.google.com/incident/cloud/sql/17012)
21:43 Nov 03, 2016
## SUMMARY:
On Monday, 31 October 2016, 73% of requests to create new subscriptions for Google Cloud Pub/Sub failed for a duration of 124 minutes. Creation of new Cloud SQL Second Generation instances also failed during this incident.
If your service or application was affected, we apologize. We have conducted a detailed review of the causes of this incident and are ensuring that we apply the appropriate fixes so that it will not recur.
## DETAILED DESCRIPTION OF IMPACT:
On Monday, 31 October 2016 from 13:11 to 15:15 PDT, 73% of requests to create new subscriptions for Google Cloud Pub/Sub failed.
0.1% of pull requests experienced latencies of up to 4 minutes for end-to-end message delivery.
Creation of all new Cloud SQL Second Generation instances also failed during this incident. Existing instances were not affected.
## ROOT CAUSE:
At 13:08, a system in the Cloud Pub/Sub control plane experienced a connectivity issue to its persistent storage layer for a duration of 83 seconds. This caused a queue of storage requests to build up. When the storage layer re-connected, the queued requests were executed, which exceeded the available processing quota for the storage system. The system entered a feedback loop in which storage requests continued to queue up leading to further latency increases and more queued requests. The system was unable to exit from this state until additional capacity was added.
Creation of a new Cloud SQL Second Generation instance requires a new Cloud Pub/Sub subscription.
REMEDIATION AND PREVENTION:
Our monitoring systems detected the outage and paged oncall engineers at 13:19. We determined root cause at 14:05 and acquired additional storage capacity for the Pub/Sub control plane at 14:42. The outage ended at 15:15 when this capacity became available.
To prevent this issue from recurring, we have already increased the storage capacity for the Cloud Pub/Sub control plane. We will change the retry behavior of the control plane to prevent a feedback loop if storage quota is temporarily exceeded. We will also improve our monitoring to ensure we can determine root cause for this type of failure more quickly in future.
We apologize for the inconvenience this issue caused our customers.

# [cloud/sql/17017](https://status.cloud.google.com/incident/cloud/sql/17017)
13:00 Aug 29, 2017
## ISSUE SUMMARY:
On Tuesday 15 August 2017, Google Cloud SQL experienced issues in the europe-west1 zones for a duration of 3 hours and 35 minutes. During this time, new connections from Google App Engine (GAE) or Cloud SQL Proxy would timeout and return an error. In addition, Cloud SQL connections with ephemeral certs that had been open for more than one hour timed out and returned an error. We apologize to our customers whose projects were affected â we are taking immediate action to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 15 August 2017 from 17:20 to 20:55 PDT, 43.1% of Cloud SQL instances located in europe-west1 were unable to be managed with the Google Cloud SQL Admin API to create or make changes. Customers who connected from GAE or used the Cloud SQL Proxy (which includes most connections from Google Container Engine) were denied new connections to their database.
## ROOT CAUSE:
The issue surfaced through a combination of a spike in error rates internal to the Cloud SQL service and a lack of available resources in the Cloud SQL control plane for europe-west1.
By way of background, the Cloud SQL system uses a database to store metadata for customer instances.  This metadata is used for validating new connections. Validation will fail if the load on the database is heavy.
In this case, Cloud SQLâs automatic retry logic overloaded the control plane and consumed all the available Cloud SQL control plane processing in europe-west1.  This in turn made the Cloud SQL Proxy and front end client server pairing reject connections when ACLs and certificate information stored in the Cloud SQL control plane could not be accessed.
REMEDIATION AND PREVENTION
Google engineers were paged at 17:20 when automated monitoring detected an increase in control plane errors. Initial troubleshooting steps did not sufficiently isolate the issue and reduce the database load. Engineers then disabled non-critical control plane services for Cloud SQL to shed load and allow the service to catch up. They then began a rollback to the previous configuration to bring back the system to a healthy state.
This issue has raised technical issues which hinder our intended level of service and reliability for the Cloud SQL service. We have begun a thorough investigation of similar potential failure patterns in order to avoid this type of service disruption in the future. We are adding additional monitoring to quickly detect metadata database timeouts which caused the control plane outage.  We are also working to make the Cloud SQL control plane services more resilient to metadata database latency by making the service not directly call the database for connection validation.
We realize this event may have impacted your organization and we apologize for this disruption.  Thank you again for your business with Google Cloud SQL.

# [compute/15037](https://status.cloud.google.com/incident/compute/15037)
16:58 Oct 16, 2014
## SUMMARY:
For a period of 51 minutes on Monday 13 October 2014, Google Compute Engine instances in the asia-east1 region experienced intermittent network connectivity problems, including DNS failures and loss of connectivity to other Google services. Additionally, a subset of external users in Asia were unable to connect to any Compute Engine instances. If this issue affected you or your systems, we sincerely apologize; we strive for a very high level of service and in this case we did not meet that bar.
## DETAILED DESCRIPTION OF IMPACT:
Beginning at 03:39 PDT and ending at 03:50, Compute Engine instances in the asia-east1 region were unable to resolve DNS queries.  From 03:52 until 04:30, connectivity to all Compute Engine instances was disrupted for users entering Googleâs network in Taiwan. Between 04:13 and 04:30, Compute Engine instances in the asia-east1 region were unable to contact other Google services.
All network connectivity between Compute Engine instances continued to operate normally throughout the incident.
## ROOT CAUSE:
While performing a network upgrade, Google engineers encountered a process bug in the upgrade procedure, resulting in uneven traffic distribution and a traffic overload on several links serving two datacenters in Taiwan. Google engineers were quickly alerted to the traffic overload and attempted to reroute traffic away from the affected datacenters. The initial attempt uncovered a latent bug in our network control plane software that prevented a load balancer from withdrawing all routes. Traffic continued to be routed to this device, which became overwhelmed.
REMEDIATION AND PREVENTION:
Upon receiving alerts of network overload in the affected datacenters, Google network engineers responded within 5 minutes to withdraw routes to these datacenters. When this did not have the desired effect, the engineers redirected traffic around the misbehaving network components. At 04:28, Google engineers resolved the underlying issue by manually disabling the faulty control plane software.
The issue in the upgrade procedure has been identified and fixed.  The bug in the network control plane software has been identified and Google engineers are currently developing and testing a fix.  Google engineers are augmenting the Compute Engine network monitoring to quickly and accurately pinpoint network issues affecting Compute Engine instances.  Finally, Google engineers are improving the way traffic is routed to and from Compute Engine instances to better segment the systemâs network failure domains.

# [compute/15039](https://status.cloud.google.com/incident/compute/15039)
10:56 Nov 05, 2014
## SUMMARY:
On Friday 31 October 2014, consumers of the Google Compute Engine API experienced increased latency and error rates for a duration of 115 minutes. Additionally, some requests to create new projects were delayed up to 4 hours. We apologize if this incident had an impact on your service or application. We have taken immediate steps to improve APIâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
From Friday 31 October at 23:50 PST until Saturday 1 November 2014 at 01:45 PDT Google Compute Engine API consumers experienced increased latency of up to 120 seconds per call along with rates of 500 and 503 responses as high as 1%. Users trying to create projects between 23:53 and 02:30 experienced delays lasting until 03:55.
## ROOT CAUSE:
A scheduled maintenance task began running at 23:45 to clean up resources linked to deleted projects. The maintenance task consumed more Compute Engine resources than expected, which caused the system to queue requests from other sources (for example, the Google Developer Console and Compute Engine APIs). Resource contention combined with a latent bug in the project creation subsystem prevented retries when API calls failed, which stopped project creation from working correctly during the outage.
REMEDIATION AND PREVENTION:
At 23:53 PST, API call latency spiked. Within one minute, Google engineers were alerted by Compute Engine monitoring systems and began investigating the spike. Within 17 minutes of the alert, Google engineers had identified the pipeline as the cause of the spike, and engaged the team responsible for it, shutting down the offending job by 00:23. Once Google engineers had stopped the job, the system took some time to process the backlog of work. API calls returned to normal latency for most users by 00:50, recovering completely by 01:45.
At 02:23, Google engineers decreased the rate at which project creations were processed, reducing contention and allowing new projects to be created successfully. Due to a latent bug, projects created during the outage remained in an incomplete state; Google engineers ran a tool to reset these incomplete projects to a pre-provisioned state, finishing at 03:55.
To prevent this class of incident from recurring, Google engineers are adding additional API quota safeguards for internal pipelines. Additionally, Google engineers will ensure that large pipeline tasks of this nature are run more frequently to avoid a large queue of tasks. To facilitate quicker identification and resolution of such incidents, Google engineers are further tuning the monitoring and alerting systems to provide extra insight into the tasks queue length for the Compute Engine subsystems involved in this incident.

# [compute/15040](https://status.cloud.google.com/incident/compute/15040)
01:33 Nov 11, 2014
## SUMMARY:
For a period of 121 minutes on Thursday 6 November 2014, all Google Compute Engine users were unable to create or delete virtual machines or persistent disks, and 17% of Compute Engine requests experienced elevated latency.  If this issue had an impact on you or your service, we apologize; we understand the standard of reliability and availability you have come to expect from Google and appreciate that we did not meet that standard in this case.  We have taken immediate steps to prevent future recurrences of this issue.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 6 November 2014 from 13:40 PST until 15:40 Compute Engine users were unable to create persistent disks, snapshots, or new instances, and were unable to delete persistent disks. Additionally, 17% of operations that do not rely on disks experienced increased latency, but failure rates did not deviate from normal levels.
## ROOT CAUSE:
Google engineers triggered a migration job to upgrade existing Compute Engine images to a new format, which involved creating a new persistent disk for each image and a new image from that disk.  This job exposed an unoptimized code path in the garbage collection portion of the persistent disk subsystem that triggered database lock contention, causing all requests to time out. A latent bug in the resource management layer of Compute Engine caused the system to retry persistent disk requests too aggressively, which amplified this contention.
REMEDIATION AND PREVENTION:
To resolve the issue, Google engineers stopped the migration job and decreased the number of tasks processing persistent disk requests, which eliminated the lock contention that had prevented those tasks from completing. Once the underlying lock contention was resolved, the backlog of tasks was cleared and requests were again served in a timely fashion.
To prevent this issue from happening in the future, Google engineers have resized the pool of workers that process persistent disk requests to prevent the lock contention from happening. Additionally, Google engineers are optimizing the persistent disk garbage collection code path to acquire locks for a shorter duration and to perform database intensive tasks in a staggered fashion, which will allow for a greater number of requests to succeed. Google engineers are also creating additional alerts that notify oncall engineers of database contention and elevated persistent disk related error rates.

# [compute/15041](https://status.cloud.google.com/incident/compute/15041)
19:34 Nov 24, 2014
## SUMMARY:
On Friday 21 November, Google Compute Engine instances in the asia-east1 region experienced elevated packet loss for 70 minutes. We sincerely apologize for the disruption in service to these instances.
## DETAILED DESCRIPTION OF IMPACT:
Beginning at 00:04 PST, Compute Engine instances in the asia-east1 region experienced up to 90% packet loss. Most packet loss was mitigated by 00:31, however traffic between instances in the europe-west1 and asia-east1 regions continued to experience 60% loss until 01:10.
## ROOT CAUSE:
This incident was caused by an unusually large surge in traffic.
REMEDIATION AND PREVENTION:
The spike in traffic was identified by Google engineers within 3 minutes of impacting other traffic. A combination of automated and manual intervention by Google engineers mitigated the majority of the impact within 45 minutes.
To most effectively handle this class of incident in the future, Google engineers are increasing the granularity of network monitoring, which will result in faster diagnosis of such issues. Google engineers are also rolling out additional automated systems to improve the way the system manages traffic when high volumes are seen.

# [compute/15042](https://status.cloud.google.com/incident/compute/15042)
16:30 Dec 22, 2014
## SUMMARY:
On Friday 19 December 2014, all Google Compute Engine instances in us-central1-a experienced elevated packet loss for a duration of 83 minutes. We apologize for the disruption.
## DETAILED DESCRIPTION OF IMPACT:
Beginning at 09:58 PST, 10% of packets to and from instances in us-central1-a were dropped. At 10:38, the drop rate increased to 60% for the next 32 minutes. At 11:10, the drop rate returned to 10% for another 10 minutes, before the end of the outage at 11:21.
## ROOT CAUSE:
The incident was caused by interference between two components of the GCE networking infrastructure during a routine software deployment.The interference began at 09:58, redirecting traffic through a lower capacity path resulting in 10% packet loss to and from instances in us-central1-a. At 10:38 the second component began rolling out, redirecting traffic to the original path with reduced capacity and increasing packet loss to 60%.
REMEDIATION AND PREVENTION:
Google engineers were notified of the issue by monitoring at 10:23. Google engineers started rolling back to the previous version 11 minutes after the packet loss increased. When the second component reverted, traffic loss was back to 10%. Finally, the engineers completed the rollback, resulting in the end of the outage.
Google engineers are eliminating the race condition in the rollout process, as well as updating related documentation and monitoring to enable faster diagnosis and remediation.

# [compute/15045](https://status.cloud.google.com/incident/compute/15045)
16:10 Feb 19, 2015
## SUMMARY:
For 40 minutes spanning Wednesday 18th and Thursday 19th February 2015, the majority of Google Compute Engine instances experienced traffic loss for outbound network connectivity, with lower levels of loss beginning at 22:40 PST on February 18th and ending at 01:20 PST on February 19th. The total length of detectable external traffic loss was 2 hours and 40 minutes. We consider GCEâs availability over the last 24 hours to be unacceptable, and we apologise if your service was affected by this outage. Today we are completely focused on addressing the incident and its root causes, so that this problem or other hypothetical similar problems cannot recur in the future.
## DETAILED DESCRIPTION OF IMPACT:
Starting at 18 February at 22:40 PST, outbound traffic from Google Compute Engine instances began to experience 10% loss of flows. The fraction of flows experiencing loss increased linearly to a peak of 70% loss at 23:55. That level of loss lasted 40 minutes until 00:35 PST on 19 February, at which point engineering remediation efforts rapidly reduced loss to 15% by 00:50. Traffic loss was eliminated and normal traffic levels resumed by 01:20.
The issue manifested as a loss of external connectivity to the instances, and an inability of the instances to send traffic outside their private network. The instances themselves continued to run, and became available again as their external traffic loss cleared.
ROOT CAUSE [PRELIMINARY]
The internal software system which programs GCEâs virtual network for VM egress traffic stopped issuing updated routing information. The cause of this interruption is still under active investigation. Cached route information provided a defense in depth against missing updates, but GCE VM egress traffic started to be dropped as the cached routes expired.
RESOLUTION AND PREVENTION
Google Engineers were alerted to the dropped packets caused by cached route expiration. 
They were able to identify a potential fix (reload the entire route information) approximately 45 minutes after being alerted, while most routing entries had not expired. They were able to force a reload to fix the networking approximately 60 minutes after the issue was identified and well before all entries had expired.
Google Engineers have already made a change to extend the expiration lifespan of routing entries from several hours to a week, which will allow ample time to take corrective action should a similar problem occur in the future. They expect to make several other more positive defense-in-depth changes to prevent recurrence in the coming days, including updates to the system which programs route information and additional monitoring and alerting. The engineering work will proceed in parallel with the completion and validation of the full post-mortem for this event.

# [compute/15046](https://status.cloud.google.com/incident/compute/15046)
14:37 Mar 08, 2015
## SUMMARY:
On Saturday March 7 2015, Google Compute Engine VMs experienced intermittent packet loss on egress network traffic between 09:55 PST to 10:38 PST.  VM execution and VM-to-VM network traffic was unaffected during this interval.
## DETAILED DESCRIPTION OF IMPACT:
Beginning March 7 2015 at 09:55 PST, Google Compute Engine traffic bound both for the Internet and other Google services experienced intermittent packet loss. The intermittent packet loss persisted for 43 minutes until 10:38 PST, at which time packet loss returned to baseline levels.  The user impact of this intermittent packet loss depended on VM, zone, and user netblock, and ranged from no visible impact, to unusually slow responses, to timeouts attempting to contact the VM.
## ROOT CAUSE:
The root cause of the packet loss was a configuration change introduced to the network stack designed to provide greater isolation between VMs and projects by capping the traffic volume allowed by an individual VM.  The configuration change had been tested prior to deployment to production without incident.  However as it was introduced into the production environment it affected some VMs in an unexpected manner.
REMEDIATION AND PREVENTION:
Automated network monitoring systems alerted Google engineers of the issue at 10:13 PST, 18 minutes after detectable packet loss first appeared.  The Google engineering team identified the root cause and rolled back the configuration change starting at 10:35 PST, which immediately decreased the incidences rate of packet loss, with full recovery complete at 10:38 PST.
Google engineers are investigating why the prior testing of the change did not accurately predict the performance of the isolation mechanism in production. Future changes will not be applied to production until the test suite has been improved to demonstrate parity with behavior observed in production during this incident.  Additionally, Google engineers are immediately amending the rollout protocol for network configuration changes so that future production changes will be applied to a small fraction of VMs at a time, reducing the exposure in the event of undetected behavior.

# [compute/15049](https://status.cloud.google.com/incident/compute/15049)
04:37 Apr 13, 2015
## SUMMARY:
On Friday 10 April 2015, Google Compute Engine instances in us-central1 experienced elevated packet loss for a duration of 14 minutes. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Friday 10 April 2015 from 02:10 to 02:24 PDT, instances hosted in Google Compute Engine zone us-central1-b experienced elevated packet loss for internal (VM <-> VM) traffic, and every zone in region us-central1 experienced elevated packet loss  for external (Internet <-> VM) traffic. The impact varied on different network paths e.g., for VM to VM and VM to Internet reported packet loss was between 26 to 47% at peak, while for Internet to VM 18 to 34% of total packets were lost.
## ROOT CAUSE:
During routine planned maintenance a miscommunication resulted in traffic being sent to a datacenter router that was running a test configuration. This resulted in a saturated link, causing packet loss. The faulty configuration became effective at 02:10 and caused traffic congestion soon after.
REMEDIATION AND PREVENTION:
Google Engineers were notified by our alerting systems at 02:12 and confirmed an unusually high rate of packet loss at 02:18. At 02:21 Google Engineers disabled the problematic router, distributing traffic to other, unsaturated links. Normal operation was restored at 02:24.
To prevent similar incidents in future, we are changing procedure to include additional validation checks while configuring routers during maintenance activities. We are also implementing a higher degree of automation to remove potential human and communication errors when changing router configurations.

# [compute/15050](https://status.cloud.google.com/incident/compute/15050)
18:11 Apr 13, 2015
## SUMMARY:
On Sunday 12th April 2015, Google Compute Engine instances in us-central1 and asia-east1 experienced intermittent 0 to 4 percent packet loss on outgoing external traffic for an overall duration of 6 hours. This was followed by a peak of up to 20 percent packet loss for a duration of 13 minutes. We apologize to our customers who were affected by this issue, and are working to address the factors that allowed this to happen.
## DETAILED DESCRIPTION OF IMPACT:
On Sunday 12th April 2015 from 16:26 to 22:24 PDT, Compute Engine experienced packet loss totalling 0 to 4 percent of traffic to external addresses. Individual instances could have experienced up to 100 percent loss intermittently. The duration of packet loss was zone-specific. The issue began in us-central1-a at 16:26 and lasted until 22:24. The zones us-central1-b, us-central1-f, and asia-east1-a experienced loss between 19:20 and 20:20.
Total loss ranged from 2 to 4 percent between 19:27 and 20:03, and 2 to 20 percent between 22:20 and 22:40. Outside these time periods, loss was under 2 percent of total egress traffic.
## ROOT CAUSE:
An abrupt increase in traffic from several large projects triggered Compute Engine's traffic shaping mechanisms. These mechanisms had an unintended spillover effect on other projects, causing some packet loss even for uninvolved projects.
REMEDIATION AND PREVENTION:
Google engineers increased the traffic capacity dedicated to Compute Engine to address the usage increase and eliminate packet loss. Googleâs engineers are also making code changes to improve the fidelity and speed of response of the traffic shaping mechanism, and eliminate packet loss for uninvolved projects in future traffic shaping events.

# [compute/15052](https://status.cloud.google.com/incident/compute/15052)
11:46 Apr 28, 2015
## SUMMARY:
From Saturday 25 April 2015 23:15 PDT to Sunday 26 April 2015 02:14 PDT, 7.4% of Google Compute Engine (GCE) instances in the asia-east1-a zone experienced networking issues. Affected instances were those either created or live migrated during the incident, and were subsequently unable to communicate on the network. Google Engineers resolved the network issues on Sunday 26 April 2015 at 02:14. We apologize to the affected customers and are implementing preventative measures to ensure similar incidents do not occur in the future.
DETAILED IMPACT:
Beginning on Saturday 25 April 2015 at 23:15, the GCE network control plane stopped propagating network configuration changes to the instance provisioning component. As a result, any instances that were created or live migrated during this time were unable to obtain valid network configuration and thus could not communicate on the network. Overall, the outgoing network traffic in the asia-east1-a zone was 25% lower than expected. Instances in other zones were unaffected. During the incident, network and HTTP load balancing correctly marked the affected instances as unhealthy and routed requests to instances in other zones if they were available.
## ROOT CAUSE:
During a scheduled maintenance event in the asia-east1 region, a latent configuration issue resulted in a network control plane component failing to restart correctly. Automated monitoring alerted Google Engineers to the issue, and after investigation they discovered and corrected the configuration problem allowing the network control plane to start and to begin propagating network configuration.
REMEDIATION AND PREVENTION:
To prevent similar incidents, Google Engineers are currently auditing the configuration of all critical GCE components to ensure they can migrate successfully. In addition, Google Engineers are implementing more aggressive monitoring to ensure more rapid remediation of issues.

# [compute/15053](https://status.cloud.google.com/incident/compute/15053)
23:28 May 12, 2015
## SUMMARY:
On Tuesday 12 May 2015 an infrastructure event caused the reboot of 6% of virtual machines in the Google Compute Engine zone us-central1-a. In addition, API operations targeting the us-central1-a zone resulted in errors for a duration of 1 hour and 38 minutes, while other Compute Engine API operations experienced elevated latency for the same duration. If you or your customers were affected by either the reboots or the API issues, we apologize. We failed to contain the issue to the affected power hardware and are working to improve the failure isolation of the systems involved.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 12 May 2015 at 02:58 PDT, 6% of virtual machines in the us-central1-a zone rebooted due to a power domain failure. The affected instances finished rebooting by 03:35 PDT.
At 03:21 PDT, Compute Engine API operations began to fail for the us-central1-a zone, and other Compute Engine API operations experienced higher than usual latency. The API issue was resolved at 04:59 PDT and API latency recovered by 05:12 PDT.
## ROOT CAUSE:
At 02:58 PDT power systems in the us-central1-a zone initiated a shutdown for safety reasons, and alerted Google engineers to the issue. In response to the power issue Google engineers initiated a change at 03:15 PDT intended to direct lower priority traffic away from us-central1-a during the event. However, a software bug in the GCE control plane interacted poorly with this change and caused API requests directed to us-central1-a to be rejected starting at 03:21 PDT. Retries and timeouts from the failed calls caused increased load on other API backends, resulting in higher latency for all GCE API calls. The API issues were resolved when Google engineers identified the control plane issue and corrected it at 04:59 PDT, with the backlog fully cleared by 05:12 PDT.
REMEDIATION AND PREVENTION:
Google engineers are fixing the bug in the control plane software so it will not unintentionally reject requests in similar situations in future. Google engineers have manually validated the configuration of the components of the API system to ensure that no similar errors will happen in the future. Google engineers will also improve the robustness of the API backends so that a single zone failure does not manifest increased latency outside of the affected zone.

# [compute/15055](https://status.cloud.google.com/incident/compute/15055)
12:47 Aug 05, 2015
## SUMMARY:
On Tuesday 4 August 2015, incoming network traffic to Google Compute Engine (GCE) was interrupted for 5 minutes. We are sorry for any impact this had on our customers' services. We have identified the cause of the incident and we are taking steps to avoid this class of problems in future.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 4 August 2015 from 08:56 to 09:01 PDT, all incoming network packets from the Internet to GCE public IP addresses were dropped. The incident affected network load balancers and Google Cloud VPNs as well as the external IP addresses of GCE instances.
Whilst packets from GCE to the Internet were not affected, the loss of return traffic prevented the correct operation of TCP connections. There was no effect on instance-to-instance traffic using GCE internal IP addresses.
## ROOT CAUSE:
GCE's external network connectivity is provided by a Google core networking component that supports many of Google's public services. A software deployment for this system introduced a bug which failed to handle a specific property of the configuration for GCE IP addresses. This led to the removal of all inward-bound routes for GCE.
REMEDIATION AND PREVENTION:
The impact on GCE networking triggered immediate alerts, and Google engineers restored service by rolling back the software deployment.
To avoid regression of the specific issue, Google engineers will extend testing frameworks to include the GCE configuration property that triggered the bug.
To increase our defence in depth against related issues in future, Google engineers will also implement a number of technical and procedural measures, including: increased engineer review of configuration changes, automatic sanity-checks on route deployment changes, and protection of IP ranges associated with GCE.

# [compute/15056](https://status.cloud.google.com/incident/compute/15056)
02:18 Aug 18, 2015
## SUMMARY:
From Thursday 13 August 2015 to Monday 17 August 2015, errors occurred on a small proportion of Google Compute Engine persistent disks in the europe-west1-b zone. The affected disks sporadically returned I/O errors to their attached GCE instances, and also typically returned errors for management operations such as snapshot creation. In a very small fraction of cases (less than 0.000001% of PD space in europe-west1-b), there was permanent data loss.
Google takes availability very seriously, and the durability of storage is our highest priority. We apologise to all our customers who were affected by this exceptional incident. We have conducted a thorough analysis of the issue, in which we identified several contributory factors across the full range of our hardware and software technology stack, and we are working to improve these to maximise the reliability of GCE's whole storage layer.
## DETAILED DESCRIPTION OF IMPACT:
From 09:19 PDT on Thursday 13 August 2015, to Monday 17 August 2015, some Standard Persistent Disks in the europe-west1-b zone began to return sporadic I/O errors to their connected GCE instances. In total, approximately 5% of the Standard Persistent Disks in the zone experienced at least one I/O read or write failure during the course of the incident. Some management operations on the affected disks also failed, such as disk snapshot creation.
From the start of the incident, the number of affected disks progressively declined as Google engineers carried out data recovery operations. By Monday 17 August, only a very small number of disks remained affected, totalling less than 0.000001% of the space of allocated persistent disks in europe-west1-b. In these cases, full recovery is not possible.
The issue only affected Standard Persistent Disks that existed when the incident began at 09:19 PDT. There was no effect on Standard Persistent Disks created after 09:19. SSD Persistent Disks, disk snapshots, and Local SSDs were not affected by the incident. In particular, it was possible at all times to recreate new Persistent Disks from existing snapshots.
## ROOT CAUSE:
At 09:19 PDT on Thursday 13 August 2015, four successive lightning strikes on the local utilities grid that powers our European datacenter caused a brief loss of power to storage systems which host disk capacity for GCE instances in the europe-west1-b zone. Although automatic auxiliary systems restored power quickly, and the storage systems are designed with battery backup, some recently written data was located on storage systems which were more susceptible to power failure from extended or repeated battery drain. In almost all cases the data was successfully committed to stable storage, although manual intervention was required in order to restore the systems to their normal serving state. However, in a very few cases, recent writes were unrecoverable, leading to permanent data loss on the Persistent Disk.
This outage is wholly Google's responsibility. However, we would like to take this opportunity to highlight an important reminder for our customers: GCE instances and Persistent Disks within a zone exist in a single Google datacenter and are therefore unavoidably vulnerable to datacenter-scale disasters. Customers who need maximum availability should be prepared to switch their operations to another GCE zone. For maximum durability we recommend GCE snapshots and Google Cloud Storage as resilient, geographically replicated repositories for your data.
REMEDIATION AND PREVENTION:
Google has an ongoing program of upgrading to storage hardware that is less susceptible to the power failure mode that triggered this incident. Most Persistent Disk storage is already running on this hardware.
Since the incident began, Google engineers have conducted a wide-ranging review across all layers of the datacenter technology stack, from electrical distribution systems through computing hardware to the software controlling the GCE persistent disk layer. Several opportunities have been identified to increase physical and procedural resilience, including:
Continue to upgrade our hardware to improve cache data retention during transient power loss.
Implement multiple orthogonal schemes to increase Persistent Disk data durability for greater resilience.
Improve response procedures for system engineers during possible future incidents.

# [compute/15057](https://status.cloud.google.com/incident/compute/15057)
13:26 Oct 30, 2015
## SUMMARY:
On Tuesday 27 October 2015, Google Compute Engine instances created within a 90 minute period in us-central1 and asia-east1 regions took longer than usual to obtain external network connectivity. Existing instances in the specified regions were not affected and continued to be available. We know how important it is to be able to create instances both for new deployments and scaling existing deployments, and we apologize for the impairment of these actions.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 27 October 2015 GCE instances created between 21:44 and 23:13 PDT in the us-central1 and asia-east1 regions took over 5 minutes before they started to receive traffic via their external IP address or network load balancer. Existing instances continued to operate without any issue, and there was no effect on internal networking for any instance.
## ROOT CAUSE:
This issue was triggered by rapid changes in external traffic patterns. The networking infrastructure automatically reconfigured itself to adapt to the changes, but the reconfiguration involved processing a substantial queue of modifications. The network registration of new GCE instances was required to wait on events in this queue, leading to delays in registration.
REMEDIATION AND PREVENTION:
This issue was resolved as the backlog of network configuration changes was automatically processed.
Google engineers will decouple the GCE networking operations and management systems that were involved in the issue such that a backlog in one system does not affect the other.
Although the issue was detected promptly, Google engineers have identified opportunities to further improve internal monitoring and alerting for related issues.

# [compute/15058](https://status.cloud.google.com/incident/compute/15058)
22:00 Nov 04, 2015
## SUMMARY:
Between Saturday 31 October 2015 and Sunday 1 November 2015, Google Compute Engine networking in the us-central1-b zone was impaired on 3 occasions for an aggregate total of 4 hours 10 minutes. We apologize if your service was affected in one of these incidents, and we are working to improve the platformâs performance and availability to meet our customerâs expectations.
DETAILED DESCRIPTION OF IMPACT (All times in Pacific/US):
Outage timeframes for Saturday 31 October 2015: 05:52 to 07:05 for 73 minutes
Outage timeframes for Sunday 1 November 2015: 14:10 to 15:30 for 80 minutes, 19:03 to 22:40 for 97 minutes
During the affected timeframes, up to 14% of the VMs in us-central1-b experienced up to 100% packet loss communicating with other VMs in the same project.  The issue impacted both in-zone and intra-zone communications.
## ROOT CAUSE:
Google network control fabrics are designed to permit simultaneous failure of one or more components.  When such failures occur, redundant components on the network may assume new roles within the control fabric.  A race condition in one of these role transitions resulted in the loss of flow information for a subset of the VMs controlled by the fabric.
REMEDIATION AND PREVENTION:
Google engineers began rolling out a change to eliminate this race condition at 18:03 PST on Monday November 2 2015.  The rollout completed on at 11:13 PST on Wednesday November 4 2015.  Additionally, monitoring is being improved to reduce the time required to detect, identify and resolve problematic changes to the network control fabric.

# [compute/15059](https://status.cloud.google.com/incident/compute/15059)
17:21 Nov 03, 2015
## SUMMARY:
On Saturday 31 October 2015, Google Compute Engine (GCE) management operations experienced high latency for a duration of 181 minutes. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we have taken and are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Saturday 31 October 2015 from 18:04 to 21:05 PDT, all Google Compute Engine management operations were slow or timed out in the Google Developers Console, the gcloud tool or the Google Compute Engine API.
## ROOT CAUSE:
An issue in the handling of Google Compute Engine management operations caused requests to not complete in a timely manner, due to older operations retrying excessively and preventing newer operations from succeeding.
Once discovered, remediation steps were taken by Google Engineers to reduce the number of retrying operations, enabling recovery from the operation backlog. The incident was resolved at 21:05 PDT when all backlogged operations were processed by the Google Compute Engine management backend and latency and error rates returned to typical values.
REMEDIATION AND PREVENTION:
To detect similar situations in the future, the GCE Engineering team is implementing additional automated monitoring to detect high numbers of queued management operations and limiting the number of operation retries. Google Engineers are also enabling more robust operation handling and load splitting to better isolate system disruptions.

# [compute/15062](https://status.cloud.google.com/incident/compute/15062)
12:21 Nov 13, 2015
## SUMMARY:
On Tuesday, 10 November 2015, outbound traffic going through one of our European routers from both Google Compute Engine and Google App Engine experienced high latency for a duration of 6h43m minutes. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we have taken and are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday, 10 November 2015 from 06:30 - 13:13 PST, a subset of outbound traffic from Google Compute Engine VMs and Google App Engine instances experienced high latency.  The disruption to service was limited to outbound traffic through one of our European routers, and caused at peak 40% of all traffic being routed through this device to be dropped. This accounted for 1% of all Google Compute Engine traffic being routed from EMEA and <0.05% of all traffic for Google App Engine.
## ROOT CAUSE:
A network component failure in one of our European routers temporarily reduced network capacity in the region causing network congestion for traffic traversing this route. Although the issue was mitigated by changing the traffic priority, the problem was only fully resolved when the affected hardware was replaced.
REMEDIATION AND PREVENTION:
As soon as significant traffic congestion in the network path was detected, at 09:10 PST, Google Engineers diverted a subset of traffic away from the affected path. As this only slightly decreased the congestion, Google Engineers made a change in traffic priority which fully mitigated the problem by 13:13 PST time. The replacement of the faulty hardware resolved the problem.
To address time to resolution, Google engineers have added appropriate alerts to the monitoring of this type of router, so that similar congestion events will be spotted significantly more quickly in future. Additionally, Google engineers will ensure that capacity plans properly account for all types of traffic in single device failures. Furthermore, Google engineers will audit and augment capacity in this region to ensure sufficient redundancy is available.

# [compute/15064](https://status.cloud.google.com/incident/compute/15064)
07:21 Nov 27, 2015
## SUMMARY:
On Monday 23 November 2015, for a duration of 70 minutes, a subset of Internet destinations was unreachable from the Google Compute Engine europe-west1 region. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we have taken and are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Monday 23 November 2015 from 11:55 to 13:05 PST, a number of Internet regions (Autonomous Systems) became unreachable from Google Compute Engine's europe1-west region. The region's traffic volume decreased by 13% during the incident. The majority of affected destination addresses were located in eastern Europe and the Middle East.
Traffic to other external destinations was not affected. There was no impact on Google Compute Engine instances in any other region, nor on traffic to any destination within Google.
## ROOT CAUSE:
At 11:51 on Monday 23 November, Google networking engineers activated an additional link in Europe to a network carrier with whom Google already shares many peering links globally. On this link, the peer's network signalled that it could route traffic to many more destinations than Google engineers had anticipated, and more than the link had capacity for. Google's network responded accordingly by routing a large volume of traffic to the link. At 11:55, the link saturated and began dropping the majority of its traffic.
In normal operation, peering links are activated by automation whose safety checks would have detected and rectified this condition. In this case, the automation was not operational due to an unrelated failure, and the link was brought online manually, so the automation's safety checks did not occur.
The automated checks were expected to protect the network for approximately one hour after link activation, and normal congestion monitoring began at the end of that period. As the post-activation checks were missing, this allowed a 61-minute delay before the normal monitoring started, detected the congestion, and alerted Google network engineers.
REMEDIATION AND PREVENTION:
Automated alerts fired at 12:56. At 13:02, Google network engineers directed traffic away from the new link and traffic flows returned to normal by 13:05.
To prevent recurrence of this issue, Google network engineers are changing procedure to disallow manual link activation. Links may only be brought up using automated mechanisms, including extensive safety checks both before and after link activation. Additionally, monitoring now begins immediately after link activation, providing redundant error detection.

# [compute/15065](https://status.cloud.google.com/incident/compute/15065)
06:00 Dec 09, 2015
## SUMMARY:
On Monday 7 December 2015, Google Container Engine customers could not create external load balancers for their services for a duration of 21 hours and 38 minutes. If your service or application was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we have taken and are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
From Monday 7 December 2015 15:00 PST to Tuesday 8 December 2015 12:38 PST, Google Container Engine customers could not create external load balancers for their services. Affected customers saw HTTP 400 âinvalid argumentâ errors when creating load balancers in their Container Engine clusters. 6.7% of clusters experienced API errors due to this issue.
The issue also affected customers who deployed Kubernetes clusters in the Google Compute Engine environment.
The issue was confined to Google Container Engine and Kubernetes, with no effect on users of any other resource based on Google Compute Engine.
## ROOT CAUSE:
Google Container Engine uses the Google Compute Engine API to manage computational resources. At about 15:00 PST on Monday 7 December, a minor update to the Compute Engine API inadvertently changed the case-sensitivity of the âsessionAffinityâ enum variable in the target pool definition, and this variation was not covered by testing. Google Container Engine was not aware of this change and sent requests with incompatible case, causing the Compute Engine API to return an error status.
REMEDIATION AND PREVENTION:
Google engineers re-enabled load balancer creation by rolling back the Google Compute Engine API to its previous version. This was complete by 8 December 2015 12:38 PST.
At 8 December 2015 10:00 PST, Google engineers committed a fix to the Kubernetes public open source repository.
Google engineers will increase the coverage of the Container Engine continuous integration system to detect compatibility issues of this kind. In addition, Google engineers will change the release process of the Compute Engine API to detect issues earlier to minimize potential negative impact.

# [compute/16002](https://status.cloud.google.com/incident/compute/16002)
10:33 Feb 04, 2016
## SUMMARY:
On Wednesday 3 February 2016, one third of network connections from external sources to Google Compute Engine instances and network load balancers in the asia-east1 region experienced high rates of network packet loss for 89 minutes. We sincerely apologize to customers who were affected. We have taken and are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 3 February 2016, from 00:40 PST to 02:09 PST, one third of network connections from external sources to Google Compute Engine instances and network load balancers in the asia-east1 region experienced high rates of network packet loss. Traffic between instances within the region was not affected.
## ROOT CAUSE:
Google Compute Engine maintains a pool of systems that encapsulate incoming packets and forward them to the appropriate instance. During a regular system update, a master failover triggered a latent configuration error in two internal packet processing servers. This configuration rendered the affected packet forwarders unable to properly encapsulate external packets destined to instances.
REMEDIATION AND PREVENTION:
Google's monitoring system detected the problem within two minutes of the configuration change. Additional alerts issued by the monitoring system for the asia-east1 region negatively affected total time required to root cause and resolve the issue. At 02:09 PST, Google engineers applied a temporary configuration change to divert incoming network traffic away from the affected packet encapsulation systems and fully restore network connectivity. In parallel, the incorrect configuration has been rectified and pushed to the affected systems.
To prevent this issue from recurring, we will change the way packet processor configurations are propagated and audited, to ensure that incorrect configurations are detected while their servers are still on standby.In addition, we will make improvements to our monitoring to make it easier for engineers to quickly diagnose and pinpoint the impact of such problems.

# [compute/16003](https://status.cloud.google.com/incident/compute/16003)
14:47 Feb 25, 2016
## SUMMARY:
On Tuesday 23 February 2016, for a duration of 10 hours and 6 minutes, 7.8% of Google Compute Engine projects had reduced quotas. We know that the ability to scale is vital to our customers, and apologize for preventing you from using the resources you need.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 23 February 2016 from 06:06 to 16:12 PST, 7.8% of Google Compute Engine projects had quotas reduced. This impacted all quotas,  including number of cores, IP addresses and disk size. If reduced quota was applied to your project and your usage reached this reduced quota you would have been unable to create new resources during this incident. Any such attempt would have resulted in a QUOTA_EXCEEDED error code with message "Quota 'XX_XX' exceeded. Limit: N". Any resources that were already created were unaffected by this issue.
## ROOT CAUSE:
In order to maximize ease of use for Google Compute Engine customers, in some cases we automatically raise resource quotas. We then provide exclusions to ensure that no quotas previously raised are reduced. We occasionally tune the algorithm to determine which quotas can be safely raised. This incident occurred when one such change was made but a bug in the aforementioned exclusion process allowed some projects to have their quotas reduced.
REMEDIATION AND PREVENTION:
As soon as Google engineers identified the cause of the issue the initiating change was rolled back and quota changes were reverted. To provide faster resolution to quota related issues in the future we are creating new automated alerting and operational documentation. To prevent a recurrence of this specific issue, we have fixed the bug in the exclusion process.  To prevent similar future issues, we are also creating a dry-run testing phase to verify the impact quota system changes will have.

# [compute/16004](https://status.cloud.google.com/incident/compute/16004)
13:35 Feb 29, 2016
## SUMMARY:
On Tuesday 23 February 2015, Google Compute Engine instances in the us-central1-f zone experienced intermittent packet loss for 46 minutes. If your service or application was affected by these network issues, we sincerely apologize. A reliable network is one of our top priorities. We have taken immediate steps to remedy the issue and we are working through a detailed plan to prevent any recurrence.
## DETAILED DESCRIPTION OF IMPACT:
On 23 February 2015 from 19:56 to 20:42 PST, Google Compute Engine instances in the us-central1-f zone experienced partial loss of network traffic. The disruption had a 25% chance of affecting any given network flow (e.g. a TCP connection or a UDP exchange) which entered or exited the us-central1-f zone. Affected flows were blocked completely. All other flows experienced no disruption. Systems that experienced a blocked TCP connection were often able to establish connectivity by retrying. Connections between endpoints within the us-central1-f zone were unaffected.
## ROOT CAUSE:
Google follows a gradual rollout process for all new releases. As part of this process, Google network engineers modified a configuration setting on a group of network switches within the us-central1-f zone. The update was applied correctly to one group of switches, but, due to human error, it was also applied to some switches which were outside the target group and of a different type. The configuration was not correct for them and caused them to drop part of their traffic.
REMEDIATION AND PREVENTION:
The traffic loss was detected by automated monitoring, which stopped the misconfiguration from propagating further, and alerted Google network engineers. Conflicting signals from our monitoring infrastructure caused some initial delay in correctly diagnosing the affected switches. This caused the incident to last longer than it should have. The network engineers restored normal service by isolating the misconfigured switches.
To prevent recurrence of this issue, Google network engineers are refining configuration management policies to enforce isolated changes which are specific to the various switch types in the network. We are also reviewing and adjusting our monitoring signals in order to lower our response times.

# [compute/16005](https://status.cloud.google.com/incident/compute/16005)
16:44 Mar 09, 2016
## SUMMARY:
On Wednesday 24 February 2016, some Google Compute Engine instances in the europe-west1-c zone experienced network connectivity loss for a duration of 62 minutes. If your service or application was affected by these network issues, we sincerely apologize. We have taken immediate steps to remedy the issue and we are working through a detailed plan to prevent any recurrence.
## DETAILED DESCRIPTION OF IMPACT:
On 24 February 2016 from 11:43 to 12:45 PST, up to 17% of Google Compute Engine instances in the europe-west1-c zone experienced a loss of network connectivity.  Affected instances lost connectivity to both internal and external destinations.
## ROOT CAUSE:
The root cause of this incident was complex, involving interactions between three components of the Google Compute Engine control plane: the main configuration repository, an integration layer for networking configuration, and the low-level network programming mechanism.
Several hours before the incident on 24th February 2016, Google engineers modified the Google Compute Engine control plane in the europe-west1-c zone, migrating the management of network firewall rules from an older system to the modern integration layer.  This was a well-understood change that had been carried out several times in other zones without incident.  As on previous occasions, the migration was completed without issues.
On this occasion, however, the migrated networking configuration included a small ratio (approximately 0.002%) of invalid rules.  The GCP network programming layer is hardened against invalid or inconsistent configuration information, and continued to operate correctly in the presence of these invalid rules.
Twenty minutes before the incident, however, a remastering event occurred in the network programming layer in the europe-west1-c zone.  Events of this kind are routine but, in this case, the presence of the invalid rules in the configuration coupled with a race condition in the way the new master loads its configuration caused the new master to load its network configuration incorrectly..  The consequence, at 11:43 PST, was a loss of network programming configuration for a subset of Compute Engine instances in the zone, effectively removing their network connectivity until the configuration could be re-propagated from the central repository.
REMEDIATION AND PREVENTION
Google engineers restored service by forcing another remastering of the network programming layer, restoring a correct network configuration.
To prevent recurrence, Google engineers are fixing both the race condition which led to an incorrect configuration during mastership change, and adding alerting for the presence of invalid rules in the network configuration so that they will be detected promptly upon introduction.  The combination of these two changes provide defense in depth against future configuration inconsistency and we believe will preserve correct function of the network programming system in the face of invalid information.

# [compute/16007](https://status.cloud.google.com/incident/compute/16007)
09:31 Apr 13, 2016
## SUMMARY:
On Monday, 11 April, 2016, Google Compute Engine instances in all regions lost external connectivity for a total of 18 minutes, from 19:09 to 19:27 Pacific Time.
We recognize the severity of this outage, and we apologize to all of our customers for allowing it to occur. As of this writing, the root cause of the outage is fully understood and GCE is not at risk of a recurrence. In this incident report, we are sharing the background, root cause and immediate steps we are taking to prevent a future occurrence. Additionally, our engineering teams will be working over the next several weeks on a broad array of prevention, detection and mitigation systems intended to add additional defense in depth to our existing production safeguards.
Finally, to underscore how seriously we are taking this event, we are offering GCE and VPN service credits to all impacted GCP applications equal to (respectively) 10% and 25% of their monthly charges for GCE and VPN.  These credits exceed what we promise in the Compute Engine Service Level Agreement (https://cloud.google.com/compute/sla) or Cloud VPN Service Level Agreement (https://cloud.google.com/vpn/sla), but are in keeping with the spirit of those SLAs and our ongoing intention to provide a highly-available Google Cloud product suite to all our customers.
## DETAILED DESCRIPTION OF IMPACT:
On Monday, 11 April, 2016 from 19:09 to 19:27 Pacific Time, inbound internet traffic to Compute Engine instances was not routed correctly, resulting in dropped connections and an inability to reconnect.  The loss of inbound traffic caused services depending on this network path to fail as well, including VPNs and L3 network load balancers. Additionally, the Cloud VPN offering in the asia-east1 region experienced the same traffic loss starting at an earlier time of 18:14 Pacific Time but the same end time of 19:27.
This event did not affect Google App Engine, Google Cloud Storage, and other Google Cloud Platform products; it also did not affect internal connectivity between GCE services including VMs, HTTP and HTTPS (L7) load balancers, and outbound internet traffic.
TIMELINE and ROOT CAUSE:
Google uses contiguous groups of internet addresses -- known as IP blocks -- for Google Compute Engine VMs, network load balancers, Cloud VPNs, and other services which need to communicate with users and systems outside of Google.  These IP blocks are announced to the rest of the internet via the industry-standard BGP protocol, and it is these announcements which allow systems outside of Googleâs network to âfindâ GCP services regardless of which network they are on.
To maximize service performance, Googleâs networking systems announce the same IP blocks from several different locations in our network, so that users can take the shortest available path through the internet to reach their Google service.  This approach also enhances reliability; if a user is unable to reach one location announcing an IP block due to an internet failure between the user and Google, this approach will send the user to the next-closest point of announcement.  This is part of the internetâs fabled ability to âroute aroundâ problems, and it masks or avoids numerous localized outages every week as individual systems in the internet have temporary problems.
At 14:50 Pacific Time on April 11th, our engineers removed an unused GCE IP block from our network configuration, and instructed Googleâs automated systems to propagate the new configuration across our network.  By itself, this sort of change was harmless and had been performed previously without incident.  However, on this occasion our network configuration management software detected an inconsistency in the newly supplied configuration.  The inconsistency was triggered by a timing quirk in the IP block removal - the IP block had been removed from one configuration file, but this change had not yet propagated to a second configuration file also used in network configuration management.  In attempting to resolve this inconsistency the network management software is designed to âfail safeâ and revert to its current configuration rather than proceeding with the new configuration.  However, in this instance a previously-unseen software bug was triggered, and instead of retaining the previous known good configuration, the management software instead removed all GCE IP blocks from the new configuration and began to push this new, incomplete configuration to the network.
One of our core principles at Google is âdefense in depthâ, and Googleâs networking systems have a number of safeguards to prevent them from propagating incorrect or invalid configurations in the event of an upstream failure or bug.  These safeguards include a canary step where the configuration is deployed at a single site and that site is verified to still be working correctly, and a progressive rollout which makes changes to only a fraction of sites at a time, so that a novel failure can be caught at an early stage before it becomes widespread.  In this event, the canary step correctly identified that the new configuration was unsafe.  Crucially however, a second software bug in the management software did not propagate the canary stepâs conclusion back to the push process, and thus the push system concluded that the new configuration was valid and began its progressive rollout.
As the rollout progressed, those sites which had been announcing GCE IP blocks ceased to do so when they received the new configuration.  The fault tolerance built into our network design worked correctly and sent GCE traffic to the the remaining sites which were still announcing GCE IP blocks.  As more and more sites stopped announcing GCE IP blocks, our internal monitoring picked up two anomalies: first, the Cloud VPN in asia-east1 stopped functioning at 18:14 because it was announced from fewer sites than GCE overall, and second, user latency to GCE was anomalously rising as more and more users were sent to sites which were not close to them.  Googleâs Site Reliability Engineers started investigating the problem when the first alerts were received, but were still trying to determine the root cause 53 minutes later when the last site announcing GCE IP blocks received the configuration at 19:07.
With no sites left announcing GCE IP blocks, inbound traffic from the internet to GCE dropped quickly, reaching >95% loss by 19:09.  Internal monitors generated dozens of alerts in the seconds after the traffic loss became visible at 19:08, and the Google engineers who had been investigating a localized failure of the asia-east1 VPN now knew that they had a widespread and serious problem.  They did precisely what we train for, and decided to revert the most recent configuration changes made to the network even before knowing for sure what the problem was.  This was the correct action, and the time from detection to decision to revert to the end of the outage was thus just 18 minutes.
With the immediate outage over, the team froze all configuration changes to the network, and worked in shifts overnight to ensure first that the systems were stable and that there was no remaining customer impact, and then to determine the root cause of the problem.  By 07:00 on April 12 the team was confident that they had established the root cause as a software bug in the network configuration management software.
DETECTION, REMEDIATION AND PREVENTION:
With both the incident and the immediate risk now over, the engineering teamâs focus is on prevention and mitigation.  There are a number of lessons to be learned from this event -- for example, that the safeguard of a progressive rollout can be undone by a system designed to mask partial failures -- which yield similarly-clear actions which we will take, such as monitoring directly for a decrease in capacity or redundancy even when the system is still functioning properly.  It is our intent to enumerate all the lessons we can learn from this event, and then to implement all of the changes which appear useful.  As of the time of this writing in the evening of 12 April, there are already 14 distinct engineering changes planned spanning prevention, detection and mitigation, and that number will increase as our engineering teams review the incident with other senior engineers across Google in the coming week.  Concretely, the immediate steps we are taking include:
Monitoring targeted GCE network paths to detect if they change or cease to function;
Comparing the IP block announcements before and after a network configuration change to ensure that they are identical in size and coverage;
Semantic checks for network configurations to ensure they contain specific Cloud IP blocks.
A FINAL WORD:
We take all outages seriously, but we are particularly concerned with outages which affect multiple zones simultaneously because it is difficult for our customers to mitigate the effect of such outages.  This incident report is both longer and more detailed than usual precisely because we consider the April 11th event so important, and we want you to understand why it happened and what we are doing about it.  It is our hope that, by being transparent and providing considerable detail, we both help you to build more reliable services, and we demonstrate our ongoing commitment to offering you a reliable Google Cloud platform.
Sincerely,
Benjamin Treynor Sloss | VP 24x7 | Google

# [compute/16011](https://status.cloud.google.com/incident/compute/16011)
17:57 Jul 10, 2016
## SUMMARY:
On Tuesday, 28 June 2016 Google Compute Engine SSD Persistent Disks experienced elevated write latency and errors in one zone for a duration of 211 minutes. We would like to apologize for the length and severity of this incident. We are taking immediate steps to prevent a recurrence and improve reliability in the future.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday, 28 June 2016 from 18:15 to 21:46 PDT SSD Persistent Disks (PD) in zone us-central1-a experienced elevated latency and errors for most writes. Instances using SSD as their root partition were likely unresponsive. For instances using SSD as a secondary disk, IO latency and errors were visible to applications. Standard (i.e. non-SSD) PD in us-central1-a suffered slightly elevated latency and errors.
Latency and errors also occurred when taking and restoring from snapshots  of Persistent Disks. Disk creation operations also had elevated error rates, both for standard and SSD PD.
Persistent Disks outside of us-central1-a were unaffected.
## ROOT CAUSE:
Two concurrent routine maintenance events triggered a rebalancing of data by the distributed storage system underlying Persistent Disk. This rebalancing is designed to make maintenance events invisible to the user, by redistributing data evenly around unavailable storage devices and machines. A previously unseen software bug, triggered by the two concurrent maintenance events, meant that disk blocks which became unused as a result of the rebalance were not freed up for subsequent reuse, depleting the available SSD space in the zone until writes were rejected.
REMEDIATION AND PREVENTION:
The issue was resolved when Google engineers reverted one of the maintenance events that triggered the issue. A fix for the underlying issue is already being tested in non-production zones.
To reduce downtime related to similar issues in future, Google engineers are refining automated monitoring such that, if this issue were to recur, engineers would be alerted before users saw impact. We are also improving our automation to better coordinate different maintenance operations on the same zone to reduce the time it takes to revert such operations if necessary.

# [compute/16012](https://status.cloud.google.com/incident/compute/16012)
21:12 Jun 30, 2016
## SUMMARY:
On Wednesday 29 June 2016, newly created Google Compute Engine instances and newly created network load balancers in all zones were partially unreachable for a duration of 106 minutes. We know that many customers depend on the ability to rapidly deploy and change configurations, and apologise for our failure to provide this to you during this time.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 29 June 2016, from 11:58 PST until 13:44 US/Pacific, new Google Compute Engine instances and new network load balancers were partially unreachable via the network.  In addition, changes to existing network load balancers were only partially applied. The level of unreachability depended on traffic path rather than instance or load balancer location. Overall, the average impact on new instances was 50% of traffic in the US and around 90% in Asia and Europe.
Existing and unchanged instances and load balancers were unaffected.
## ROOT CAUSE:
On 11:58 PST, a scheduled upgrade to Googleâs network control system started, introducing an additional access control check for network configuration changes. This inadvertently removed the access of GCEâs management system to network load balancers in this environment. Only a fraction of Google's network locations require this access as an older design has an intermediate component doing access updates. As a result these locations did not receive updates for new and changed instances or load balancers.
The change was only tested at network locations that did not require the direct access, which resulted in the issue not being detected during testing and canarying and being deployed globally.
REMEDIATION AND PREVENTION:
After identifying the root cause, the access control check was modified to allow access by  GCEâs management system. The issue was resolved when this modification was fully deployed.
To prevent future incidents, the network team is making several changes to their deployment processes. This will improve the level of testing and canarying to catch issues earlier, especially where an issue only affects a subset of the environments at Google. The deployment process will have the rollback procedure enhanced to allow the quickest possible resolution for future incidents.
The access control system that was at the root of this issue will also be modified to improve operations that interacts with it. For example it will be integrated with a Google-wide change logging system to allow faster detection of issues caused by access control changes. It will also be outfitted with a dry run mode to allow consequences of changes to be tested during development time.
Once again we would like to apologise for falling below the level of service you rely on.

# [compute/16015](https://status.cloud.google.com/incident/compute/16015)
07:21 Aug 09, 2016
## SUMMARY:
On Friday 5 August 2016, some Google Cloud Platform customers experienced increased network latency and packet loss to Google Compute Engine (GCE), Cloud VPN, Cloud Router and Cloud SQL, for a duration of 99 minutes. If you were affected by this issue, we apologize. We intend to provide a higher level reliability than this, and we are working to learn from this issue to make that a reality.
## DETAILED DESCRIPTION OF IMPACT:
On Friday 5th August 2016 from 00:55 to 02:34 PDT a number of services were disrupted:
Some Google Compute Engine TCP and UDP traffic had elevated latency. Most ICMP, ESP, AH and SCTP traffic inbound from outside the Google network was silently dropped, resulting in existing connections being dropped and new connections timing out on connect.
Most Google Cloud SQL first generation connections from sources external to Google failed with a connection timeout. Cloud SQL second generation connections may have seen higher latency but not failure.
Google Cloud VPN tunnels remained connected, however there was complete packet loss for data through the majority of tunnels. As Cloud Router BGP sessions traverse Cloud VPN, all sessions were dropped.
All other traffic was unaffected, including internal connections between Google services and services provided via HTTP APIs.
## ROOT CAUSE:
While removing a faulty router from service, a new procedure for diverting traffic from the router was used. This procedure applied a new configuration that resulted in announcing some Google Cloud Platform IP addresses from a single point of presence in the southwestern US. As these announcements were highly specific they took precedence over the normal routes to Google's network and caused a substantial proportion of traffic for the affected network ranges to be directed to this one point of presence. This misrouting directly caused the additional latency some customers experienced.
Additionally this misconfiguration sent affected traffic to next-generation infrastructure that was undergoing testing. This new infrastructure was not yet configured to handle Cloud Platform traffic and applied an overly-restrictive packet filter. This blocked traffic on the affected IP addresses that was routed through the affected point of presence to Cloud VPN, Cloud Router, Cloud SQL first generation and GCE on protocols other than TCP and UDP.
REMEDIATION AND PREVENTION:
Mitigation began at 02:04 PDT when Google engineers reverted the network infrastructure change that caused this issue, and all traffic routing was back to normal by 02:34. The system involved was made safe against recurrences by fixing the erroneous configuration. This includes changes to BGP filtering to prevent this class of incorrect announcements.
We are implementing additional integration tests for our routing policies to ensure configuration changes behave as expected before being deployed to production. Furthermore, we are improving our production telemetry external to the Google network to better detect peering issues that slip past our tests.
We apologize again for the impact this issue has had on our customers.

# [compute/16017](https://status.cloud.google.com/incident/compute/16017)
18:19 Aug 30, 2016
## SUMMARY:
On Monday 22 August 2016, the Google Cloud US-CENTRAL1-F zone lost network connectivity to services outside that zone for a duration of 25 minutes. All other zones in the US-CENTRAL1 region were unaffected. All network traffic within the zone was also unaffected.
We apologize to customers whose service or application was affected by this incident. We understand that a network disruption has a negative impact on your application - particularly if it is homed in a single zone - and we apologize for the inconvenience this caused. What follows is our detailed analysis of the root cause and actions we will take in order to prevent this type of incident from recurring.
## DETAILED DESCRIPTION OF IMPACT:
We have received feedback from customers asking us to specifically and separately enumerate the impact of incidents to any service that may have been touched. We agree that this will make it easier to reason about the impact of any particular event and we have done so in the following descriptions.
On Monday 22 August 2016 from 07:05 to 07:30 PDT the Google Cloud US-CENTRAL1-F zone lost network connectivity to services outside that zone.
App Engine
6% of App Engine Standard Environment applications in the US-CENTRAL region served elevated error rates for up to 8 minutes, until the App Engine serving infrastructure automatically redirected traffic to a failover zone. The aggregate error rate across all impacted applications during the incident period was 3%. The traffic redirection caused a Memcache flush for affected applications, and also loading requests as new instances of the applications started up in the failover zones.
All App Engine Flexible Environment applications deployed to the US-CENTRAL1-F zone were unavailable for the duration of the incident. Additionally, 4.5% of these applications experienced various levels of unavailability for up to an additional 5 hours while the system recovered.
Deployments for US-CENTRAL Flexible applications were delayed during the incident. Our engineers disabled the US-CENTRAL1-F zone for new deployments during the incident, so that any customers who elected to redeploy, immediately recovered.
Cloud Console
The Cloud Console was available during the incident, though some App Engine administrative pages did not load for applications in US-CENTRAL and 50% of project creation requests failed to complete and needed to be retried by customers before succeeding.
Cloud Dataflow
Some Dataflow running jobs in the US-CENTRAL1 region experienced delays in processing. Although most of the affected jobs recovered gracefully after the incident ended, up to 2.5% of affected jobs in this zone became stuck and required manual termination by customers. New jobs created during the incident were not impacted.
Cloud SQL
Cloud SQL First Generation instances were not impacted by this incident.
30% of Cloud SQL Second Generation instances in US-CENTRAL1 were unavailable for up to 5 minutes, after which they became available again. An additional 15% of Second Generation instances were unavailable for 22 minutes.
Compute Engine
All instances in the US-CENTRAL1-F zone were inaccessible from outside the zone for the duration of the incident. 9% of them remained inaccessible from outside the zone for an additional hour.
Container Engine
Container Engine clusters running in US-CENTRAL1-F were inaccessible from outside of the zone during the incident although they continued to serve.
In addition, calls to the Container Engine API experienced a 4% error rate and elevated latency during the incident, though this was substantially mitigated if the client retried the request.
Stackdriver Logging
20% of log API requests sent to Stackdriver Logging in the US-CENTRAL1 region failed during the incident, though App Engine logging was not impacted. Clients retrying requests recovered gracefully.
Stackdriver Monitoring
Requests to the StackDriver web interface and the Google Monitoring API v2beta2 and v3 experienced elevated latency and an error rate of up to 3.5% during the incident. In addition, some alerts were delayed. Impact for API calls was substantially mitigated if the client retried the request.
## ROOT CAUSE:
On 18 July, Google carried out a planned maintenance event to inspect and test the UPS on a power feed in one zone in the US-CENTRAL1 region. That maintenance disrupted one of the two power feeds to network devices that control routes into and out of the US-CENTRAL1-F zone.
Although this did not cause any disruption in service, these devices unexpectedly and silently disabled the affected power supply modules - a previously unseen behavior. Because our monitoring systems did not notify our network engineers of this problem the power supply modules were not re-enabled after the maintenance event.
The service disruption was triggered on Monday 22 August, when our engineers carried out another planned maintenance event that removed power to the second power feed of these devices, causing them to disable the other power supply module as well, and thus completely shut down.
Following our standard procedure when carrying out maintenance events, we made a detailed line walk of all critical equipment prior to, and after, making any changes. However, in this case we did not detect the disabled power supply modules.
Loss of these network devices meant that machines in US-CENTRAL1-F did not have routes into and out of the zone but could still communicate to other machines within the same zone.
REMEDIATION AND PREVENTION:
Our network engineers received an alert at 07:14, nine minutes after the incident started. We restored power to the devices at 07:30. The network returned to service without further intervention after power was restored.
As immediate followup to this incident, we have already carried out an audit of all other network devices of this type in our fleet to verify that there are none with disabled power supply modules.
We have also written up a detailed post mortem of this incident and will take the following actions to prevent future outages of this type:
Our monitoring will be enhanced to detect cases in which power supply modules are disabled. This will ensure that conditions that are missed by the manual line walk prior to maintenance events are picked up by automated monitoring.
We will change the configuration of these network devices so that power disruptions do not cause them to disable their power supply modules.
The interaction between the network control plane and the data plane should be such that the data plane should "fail open" and continue to route packets in the event of control plane failures.  We will add support for networking protocols that have the capability to continue to route traffic for a short period in the event of failures in control plane components.
We will also be taking various actions to improve the resilience of the affected  services to single-zone outages, including the following:
App Engine
Although App Engine Flexible Environment is currently in Beta, we expect production services to be more resilient to single zone disruptions. We will make this extra resilience an exit criteria before we allow the service to reach General Availability.
Cloud Dataflow
We will improve resilience of Dataflow to single-zone outages by implementing better strategies for migrating the job controller to a new zone in the event of an outage. Work on this remediation is already underway.
Stackdriver Logging
We will make improvements to the Stackdriver Logging service (currently in Beta) in the areas of automatic failover and capacity management before this service goes to General Availability. This will ensure that it is resilient to single-zone outages.
Stackdriver Monitoring
The Google Monitoring API (currently in beta) is already hosted in more than one zone, but we will further improve its resilience by adding additional capacity to ensure a single-zone outage does not cause overload in any other zones. We will do this before this service exits to General Availability.
Finally, we know that you depend on Google Cloud Platform for your production workloads and we apologize for the inconvenience this event caused.

# [compute/16020](https://status.cloud.google.com/incident/compute/16020)
13:15 Oct 18, 2016
## SUMMARY:
On Thursday 13 October 2016, approximately one-third of requests sent to the Google Compute Engine HTTP(S) Load Balancers between 15:07 and 17:25 PDT received an HTTP 502 error rather than the expected response. If your service or application was affected, we apologize. We took immediate action to restore service once the problem was detected, and are taking steps to improve the Google Compute Engine HTTP(S) Load Balancerâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
Starting at 15:07 PDT on Thursday 13 October 2016, Google Compute Engine HTTP(S) Load Balancers started to return elevated rates of HTTP 502 (Bad Gateway) responses. The error rate rose progressively from 2% to a peak of 45% of all requests at 16:09 and remained there until 17:03. From 17:03 to 17:15, the error rate declined rapidly from 45% to 2%. By 17:25 requests were routing as expected and the incident was over. During the incident, the error rate seen by applications using GCLB varied depending on the network routing of their requests to Google.
## ROOT CAUSE:
The Google Compute Engine HTTP(S) Load Balancer system is a global, geographically-distributed multi-tiered software stack which receives incoming HTTP(S) requests via many points in Google's global network, and dispatches them to appropriate Google Compute Engine instances. On 13 October 2016, a configuration change was rolled out to one of these layers with widespread distribution beginning at 15:07. This change triggered a software bug which decoupled second-tier load balancers from a number of first-tier load balancers. The affected first-tier load balancers therefore had no forwarding path for incoming requests and returned the HTTP 502 code to indicate this.
Googleâs networking systems have a number of safeguards to prevent them from propagating incorrect or invalid configurations, and to reduce the scope of the impact in the event that a problem is exposed in production. These safeguards were partially successful in this instance, limiting both the scope and the duration of the event, but not preventing it entirely. The first relevant safeguard is a canary deployment, where the configuration is deployed at a single site and that site is verified to be functioning within normal bounds. In this case, the canary step did generate a warning, but it was not sufficiently precise to cause the on-call engineer to immediately halt the rollout. The new configuration subsequently rolled out in stages, but was halted part way through as further alerts indicated that it was not functioning correctly.  By design, this progressive rollout limited the error rate experienced by customers.
REMEDIATION AND PREVENTION:
Once the nature and scope of the issue became clear, Google engineers first quickly halted and reverted the rollout. This prevented a larger fraction of GCLB instances from being affected.  Google engineers then set about restoring function to the GCLB instances which had been exposed to the configuration.  They verified that restarting affected GCLB instances restored the pre-rollout configuration, and then rapidly restarted all affected GCLB instances, ending the event.
One of our guiding principles for avoiding large-scale incidents is to roll out global changes slowly and carefully monitor for errors. We typically have a period of soak time during a canary release before rolling out more widely. In this case, the change was pushed too quickly for accurate detection of the class of failure uncovered by the configuration being rolled out. We will change our processes to be more conservative when rolling out configuration changes to critical systems.
As defense in depth, Google engineers are also changing the black box monitoring for GCLB so that it will test the first-tier load balancers impacted by this incident. We will also be improving the black box monitoring to ensure that our probers cover all use cases. In addition, we will add an alert for elevated error rates between first-tier and second-tier load balancers.
We apologize again for the impact this issue caused our customers.

# [compute/17003](https://status.cloud.google.com/incident/compute/17003)
18:30 Feb 08, 2017
## ISSUE SUMMARY:
On Monday 30 January 2017, newly created Google Compute Engine instances, Cloud VPNs and network load balancers were unavailable for a duration of 2 hours 8 minutes. We understand how important the flexibility to launch new resources and scale up GCE is for our users and apologize for this incident. In particular, we apologize for the wide scope of this issue and are taking steps to address the scope and duration of this incident as well as the root cause itself.
## DETAILED DESCRIPTION OF IMPACT:
Any GCE instances, Cloud VPN tunnels or GCE network load balancers created or live migrated on Monday 30 January 2017 between 10:36 and 12:42 PDT were unavailable via their public IP addresses until the end of that period. This also prevented outbound traffic from affected instances and load balancing health checks from succeeding. Previously created VPN tunnels, load balancers and instances that did not experience a live migration were unaffected.
## ROOT CAUSE:
All inbound networking for GCE instances, load balancers and VPN tunnels enter via shared layer 2 load balancers. These load balancers are configured with changes to IP addresses for these resources, then automatically tested in a canary deployment, before changes are globally propagated.
The issue was triggered by a large set of updates which were applied to a rarely used load balancing configuration. The application of updates to this configuration exposed an inefficient code path which resulted in the canary timing out. From this point all changes of public addressing were queued behind these changes that could not proceed past the testing phase.
REMEDIATION AND PREVENTION
To resolve the issue, Google engineers restarted the jobs responsible for programming changes to the network load balancers. After restarting, the problematic changes were processed in a batch, which no longer reached the inefficient code path. From this point updates could be processed and normal traffic resumed. This fix was applied zone by zone between 11:36 and 12:42.
To prevent this issue from reoccurring in the short term, Google engineers are increasing the canary timeout so that updates exercising the inefficient code path merely slow network changes rather than completely stop them. As a long term resolution, the inefficient code path is being improved, and new tests are being written to test behaviour on a wider range of configurations.
Google engineers had already begun work to replace global propagation of address configuration with decentralized routing. This work is being accelerated as it will prevent issues with this layer having global impact.
Google engineers are also creating additional metrics and alerting that will allow the nature of this issue to be identified sooner, which will lead to faster resolution.

# [compute/17007](https://status.cloud.google.com/incident/compute/17007)
14:11 Apr 12, 2017
## ISSUE SUMMARY:
On Wednesday 5 April 2017, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes.
We apologize for this incident. We understand that the Load Balancer needs to be very reliable for you to offer a high quality service to your customers. We have taken and will be taking various measures to prevent this type of incident from recurring.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 5 April 2017 from 01:13 to 01:35 PDT, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes. Clients received 502 errors for failed requests. Some HTTP(S) Load Balancers that were recently modified experienced error rates of 100%.
Google paused all configuration changes to the HTTP(S) Load Balancer for three hours and 41 minutes after the incident, until our engineers had understood the root cause. This caused deployments of App Engine Flexible apps to fail during that period.
## ROOT CAUSE:
A bug in the HTTP(S) Load Balancer configuration update process caused it to revert to a configuration that was substantially out of date.
The configuration update process is controlled by a master server. In this case, one of the replicas of the master servers lost access to Google's distributed file system and was unable to read recent configuration files. Mastership then passed to the server that could not access Google's distributed file system. When the mastership changes, it begins the next configuration push as normal by testing on a subset of HTTP(S) Load Balancers. If this test succeeds, the configuration is pushed globally to all HTTP(S) Load Balancers.  If the test fails (as it did in this case), the new master will revert all HTTP(S) Load Balancers to the last "known good" configuration. The combination of a mastership change, lack of access to more recent updates, and the initial test failure for the latest config caused the HTTP(S) Load Balancers to revert to the latest configuration that the master could read, which was substantially out-of-date.
In addition, the update with the out-of-date configuration triggered a garbage collection process on the Google Frontend servers to free up memory used by the deleted configurations. The high number of deleted configurations caused the Google Frontend servers to spend a large proportion of CPU cycles on garbage collection which lead to failed health checks and eventual restart of the affected Google Frontend server. Any client requests served by a restarting server received 502 errors.
REMEDIATION AND PREVENTION
Google engineers were paged at 01:22 PDT. They switched the configuration update process to use a different master server at 01:34 which mitigated the issue for most services within one minute. Our engineers then paused the configuration updates to the HTTP(S) Load Balancer until 05:16 while the root cause was confirmed.
To prevent incidents of this type in future, we are taking the following actions:

Master servers will be configured to never push HTTP(S) Load Balancer configurations that are more than a few hours old.
Google Frontend servers will reject loading a configuration file that is more than a few hours old.
Improve testing for new HTTP(S) Load Balancer configurations so that out-of-date configurations are flagged before being pushed to production.
Fix the issue that caused the master server to fail when reading files from Google's distributed file system.
Fix the issue that caused health check failures on Google Frontends during heavy garbage collection.

Once again, we apologize for the impact that this incident had on your service.

# [compute/17008](https://status.cloud.google.com/incident/compute/17008)
07:17 Jun 17, 2017
## ISSUE SUMMARY:
On Thursday 8 June 2017, from 08:24 to 09:26 US/Pacific Time, datacenters in the asia-northeast1 region experienced a loss of network connectivity for a total of 62 minutes. We apologize for the impact this issue had on our customers, and especially to those customers with deployments across multiple zones in the asia-northeast1 region. We recognize we failed to deliver the regional reliability that multiple zones are meant to achieve.
We recognize the severity of this incident and have completed an extensive internal postmortem.  We thoroughly understand the root causes and no datacenters are at risk of recurrence.  We are at work to add mechanisms to prevent and mitigate this class of problem in the future.  We have prioritized this work and in the coming weeks, our engineering team will complete the action items we have generated from the postmortem.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 8 June 2017, from 08:24 to 09:26 US/Pacific Time, network connectivity to and from Google Cloud services running in the asia-northeast1 region was unavailable for 62 minutes.  This issue affected all Google Cloud Platform services in that region, including Compute Engine, App Engine, Cloud SQL, Cloud Datastore, and Cloud Storage.  All external connectivity to the region was affected during this time frame, while internal connectivity within the region was not affected.
In addition, inbound requests from external customers originating near Googleâs Tokyo point of presence intended for Compute or Container Engine HTTP Load Balancing were lost for the initial 12 minutes of the outage. Separately, Internal Load Balancing within asia-northeast1 remained degraded until 10:23.
## ROOT CAUSE:
At the time of incident, Google engineers were upgrading the network topology and capacity of the region; a configuration error caused the existing links to be decommissioned before the replacement links could provide connectivity, resulting in a loss of connectivity for the asia-northeast1 region. Although the replacement links were already commissioned and appeared to be ready to serve, a network-routing protocol misconfiguration meant that the routes through those links were not able to carry traffic.
As Google's global network grows continuously, we make upgrades and updates reliably by using automation for each step and, where possible, applying changes to only one zone at any time.  The topology in asia-northeast1 was the last region unsupported by automation; manual work was required to be performed to align its topology with the rest of our regional deployments (which would, in turn, allow automation to function properly in the future). This manual change mistakenly did not follow the same per-zone restrictions as required by standard policy or automation, which meant the entire region was affected simultaneously.
In addition, some customers with deployments across multiple regions that included asia-northeast1 experienced problems with HTTP Load Balancing due to a failure to detect that the backends were unhealthy. When a network partition occurs, HTTP Load Balancing normally detects this automatically within a few seconds and routes traffic to backends in other regions. In this instance, due to a performance feature being tested in this region at the time, the mechanism that usually detects network partitions did not trigger, and continued to attempt to assign traffic until our on-call engineers responded.  Lastly, the Internal Load Balancing outage was exacerbated due to a software defined networking component which was stuck in a state where it was not able to provide network resolution for instances in the load balancing group.
REMEDIATION AND PREVENTION
Google engineers were paged by automated monitoring within one minute of the start of the outage, at 08:24 PDT. They began troubleshooting and declared an emergency incident 8 minutes later at 08:32. The issue was resolved when engineers reconnected the network path and reverted the configuration back to the last known working state at 09:22. Our monitoring systems worked as expected and alerted us to the outage promptly.
The time-to-resolution for this incident was extended by the time taken to perform the rollback of the network change, as the rollback had to be performed manually.  We are implementing a policy change that any manual work on live networks be constrained to a single zone. This policy will be enforced automatically by our change management software when changes are planned and scheduled.  In addition, we are building automation to make these types of changes in future, and to ensure the system can be safely rolled back to a previous known-good configuration at any time during the procedure.
The fix for the HTTP Load Balancing performance feature that caused it to incorrectly believe zones within asia-northeast1 were healthy will be rolled out shortly.
SUPPORT COMMUNICATIONS
During the incident, customers who had originally contacted Google Cloud Support in Japanese did not receive periodic updates from Google as the event unfolded. This was due to a software defect in the support tooling â unrelated to the incident described earlier.
We have already fixed the software defect, so all customers who contact support will receive incident updates.  We apologize for the communications gap to our Japanese-language customers.
RELIABILITY SUMMARY
One of our biggest pushes in GCP reliability at Google is a focus on careful isolation of zones from each other.  As we encourage users to build reliable services using multiple zones, we also treat zones separately in our production practices, and we enforce this isolation with software and policy.  Since we missed this markâand affecting all zones in a region is an especially serious outageâwe apologize.  We intend for this incident report to accurately summarize the detailed internal post-mortem that includes final assessment of impact, root cause, and steps we are taking to prevent an outage of this form occurring again.  We hope that this incident report demonstrates the work we do to learn from our mistakes to deliver on this commitment. We will do better.
Sincerely,
Benjamin Lutch | VP Site Reliability Engineering | Google

# [compute/18012](https://status.cloud.google.com/incident/compute/18012)
10:33 Nov 09, 2018
## ISSUE SUMMARY:
On Wednesday 5 November 2018, Google Compute Engine (GCE) experienced new instance creation failures or elevated instance creation latency in us-central1-a for a duration of 5 hours. We apologize to our customers whose services or businesses were impacted during this incident, and we are taking immediate steps to avoid a recurrence.
## DETAILED DESCRIPTION OF IMPACT:
50% of new Google Compute Engine (GCE) instances failed to or were slow to create in us-central1-a on Wednesday 5 November 2018 from 04:58 - 09:46 PST. This also affected Google Kubernetes Engine (GKE) cluster creation, and instances used by Google Cloud SQL, Google Cloud Dataproc, and Google Cloud Shell in the same region. Additionally, instances that were live migrated or had operations [1] that were mutated by gcloud or from the Cloud Console during this period may have gotten into a bad state. This would have manifested as an instance being stuck and not being restartable.
[1] https://cloud.google.com/sdk/gcloud/reference/compute/operations/list
## ROOT CAUSE:
Googleâs datacenters rely on sharded Access Control Lists (ACL) stored in a highly available lock service called Chubby [1] to perform operations in the data plane. The root cause was a standard ACL update, when a job crashed mid-write, leaving the ACL stored in Chubby in a corrupted state. After an automatic restart, faulty recovery logic was triggered which prevented the corrupted ACL from being correctly re-written.This caused any operations that attempted to read the ACL to fail. As a result, the permissions of affected instances were not verifiable and the requested control plane operation eventually timed out, causing the instance creation failure, or crash-looping of instances that were being live migrated to other hosts.
[1] https://ai.google/research/pubs/pub27897
REMEDIATION AND PREVENTION
Automated alerts notified Googleâs engineering team to the event approximately 12 minutes after impact started, and they immediately began investigating. Multiple Google engineering teams were engaged, and the root cause was eventually discovered at 08:11. For mitigation, engineering took steps to ensure a thorough fix and to prevent a recurrence. By 09:46 the missing ACL had been re-written and operations immediately recovered.
In addition to addressing the root cause, we will be implementing changes to prevent, more quickly detect, mitigate, and reduce the impact of this type of failure in the future. Specifically, we are adding additional monitoring and logging to surface failures in ACL checks. Furthermore, the libraries which read ACLs will be made resilient to failure during write, eliminating this failure mode entirely.
We would again like to apologize for the impact that this incident had on our customers and their businesses in the us-central1-a zone. We are conducting a detailed post-mortem to ensure that all the root and contributing causes of this event are understood and addressed promptly.

# [developers/console/15002](https://status.cloud.google.com/incident/developers/console/15002)
06:16 Apr 10, 2015
## SUMMARY:
On Wednesday 8 April 2015, 15% of requests to the Beta Compute Engine Instance Groups and Instance Group Manager APIs failed for a duration of 5 hours. Affected projects experienced issues accessing Compute Engine pages in the Developers Console during the outage. Not all projects were impacted. If your user experience was affected, we apologize â this is not the level of quality and reliability we strive to offer you, and we have taken and are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 8 April 2015 from 11:37 to 16:35 PDT the Beta Compute Engine Instance Groups API and Instance Group Manager API returned error code 500 responses for 15% of the calls made. The Compute Engine Developers Console (http://console.developers.google.com/) pages for VM Instances, HTTP Load Balancing, and Metadata also failed for those projects due to reliance on those APIs. Users in affected projects trying to access these pages were presented with the message âService internal error occurred.". Error code: "internalErrorââ. The gcloud compute instance list command was unaffected, but gcloud commands using the Instance Groups and Instance Group Manager APIs were also affected.
## ROOT CAUSE:
A routine software upgrade to the Instance Groups and Instance Group Manager APIs increased the resource consumption of the backend servicing these APIs. As projects used the API, the backend exhausted its internal quota and was unable to service requests from new projects. Those projects whose requests succeeded before the quota had exhausted continued to use the API successfully.
REMEDIATION AND PREVENTION:
Google engineers were automatically alerted that the Instance Groups and Instance Group Manager backends were approaching an internal quota within an hour from the start of the incident. Google engineers began to revert the change that led to the increased resource consumption, and simultaneously added capacity to the service to allow it to serve new projects. The increase in quota allowed requests to the API and the Developers Console function correctly until the rollback was complete.
To prevent similar issues occurring in future Google engineers are rolling out improvements to monitoring, alerting and testing procedures. In addition, Google engineers are increasing the resilience of the Developers Console by isolating issues in backend services and APIs.

# [developers/console/15003](https://status.cloud.google.com/incident/developers/console/15003)
18:52 May 05, 2015
## SUMMARY:
On Saturday 2 May 2015, the Logs Viewer in the Google Cloud Developers Console was unavailable for a duration of 7 hours 10 minutes. We apologize to users who were affected by this issue â this is not the level of quality and reliability we strive to offer you, and we are working to improve the availability of the affected components.
## DETAILED DESCRIPTION OF IMPACT:
On Saturday 2 May 2015 from 11:10 to 18:20 PDT, the Logs Viewer in the Google Cloud Developers Console was unavailable. Users that tried to access the Logs Viewer saw a loading animation which continued indefinitely.
Log recording was not affected and messages logged during the incident were available when the Logs Viewer service was restored. Additionally, App Engine logs were still viewable in the App Engine console under appengine.google.com for the duration of the incident.
## ROOT CAUSE:
At 11:10 Google engineers deployed a networking configuration change which prevented the Logs Viewer from contacting a backend component of the Cloud logging subsystem. This change affected requests that were issued from outside the Google network.
The Cloud Developers Console has continuous monitoring to detect elevated error rates, but the monitoring submits requests from within the Google network and therefore reported that the Logs Viewer was working correctly, with the result that Google engineers did not become aware of the issue until it was reported by Cloud Platform customers.
REMEDIATION AND PREVENTION:
Google engineers identified the problematic change at 17:52 and immediately started a rollback to resolve the issue. This was complete at 18:20.
To ensure prompt detection of any similar issues in future, Google engineers are extending the monitoring and testing of the Cloud Developer Console to include probes from outside Google's network.

# [developers/console/15004](https://status.cloud.google.com/incident/developers/console/15004)
18:54 May 11, 2015
## SUMMARY:
On Friday 8 May 2015, users were unable to reliably create projects in the Google Cloud Developers Console for 6 hours 58 minutes in aggregate.  We treat the reliability and availability of the Developers Console with the highest priority and we apologize to any users who were unable to create new projects during that time.
## DETAILED DESCRIPTION OF IMPACT:
On Friday 8 May 2015, from 04:53 to 07:25 and from 09:35 to 12:31 PDT, users were unable to reliably create new projects using the Developers Console. Specifically, up to 90% of project creation requests failed and returned a "Backend Error" message to the user.  Existing projects were not affected by this incident.
ROOT CAUSE AND REMEDIATION:
A configuration change in the access management system of Developers Console triggered an existing software bug in a previously unused code path. As the change was rolled out, the access management system could no longer correctly verify userâs permissions, resulting in an error response.
Google engineers were automatically alerted to the issue at 05:04. At 05:22 a preliminary source of the issue was identified. At 09:32 the root cause was confirmed and a solution was developed.  An expedited roll-out of the fix commenced at 11:41 and completed at 12:31.

# [developers/console/15005](https://status.cloud.google.com/incident/developers/console/15005)
23:09 Jul 28, 2015
## SUMMARY:
On Monday, 27 July 2015, the Google Developers Console was unavailable to all users for a duration of 41 minutes. We apologize for the inconvenience and any impact on your operations that this may have caused. We are urgently working to implement preventative measures to ensure similar incidents do not occur in the future.
## DETAILED DESCRIPTION OF IMPACT:
On Monday, 27th July 2015 from 13:21 to 14:02 PDT, the Google Developers Console was unavailable to users. All requests tohttps://console.developers.google.comreturned a 404 "Not Found" response.
Existing Cloud Platform resources such as Compute Engine instances or App Engine applications were not affected. All Google Cloud Platform APIs remained fully functional, allowing most Cloud Platform resources to be managed through the Google Cloud SDK and other API-based tools until Console access was restored.
## ROOT CAUSE:
At 13:21, while reviewing the production status of the Developer Console, a Google engineer inadvertently disabled the production instance of the console. The engineer immediately recognised the error and began remediating the problem, but the configuration change had also engaged a security mechanism which restricted the application to the Google corporate network. This mechanism was identified and disengaged at 14:01, which restored public access to the Console.
REMEDIATION AND PREVENTION:
To prevent similar incidents, Google Engineers are currently adding safeguards to make it harder to change application settings by mistake, implementing external monitoring to detect errors outside of the Google network, and creating alerts based on serving errors from the Developers Console.

# [developers/console/16004](https://status.cloud.google.com/incident/developers/console/16004)
22:33 Feb 21, 2015
## SUMMARY:
On Thursday 19 February 2015, the Google Developers Console (https://console.developers.google.com) served a high rate of errors like âFailed to loadâ on many pages for a duration of 3 hours and 3 minutes.  This affected users in all regions to varying degrees.  If your service or application was affected, we apologize. We have taken and are taking immediate steps to improve our preparedness to mitigate and resolve similar issues in much shorter time in the future.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 19 February 2015 from 12:42 to 15:45 PST the vast majority of attempts to create new projects and interact with existing projects via the Google Developers Console failed.
## ROOT CAUSE:
The Google Developers Console relies upon a component of Google Cloud Platform's billing system to provide project details.  This component was under-provisioned for certain observed traffic patterns and suffered from contention under load, resulting in timeouts when serving user requests.
REMEDIATION AND PREVENTION:
Google engineers were automatically alerted to the issue at 12:51, and immediately began investigating. To mitigate the issue, at 13:33 Google engineers directed traffic away from the datacenter that was most heavily affected. Following further investigation, Google engineers directed traffic away from a second affected datacenter at 15:41.
In order to prevent this issue from recurring, Google engineers have made immediate increases to the available capacity in the billing system. Additionally, Google engineers are implementing changes to reduce the Developers Consoleâs dependence on the affected systems.

# [developers/console/16005](https://status.cloud.google.com/incident/developers/console/16005)
04:11 Jul 06, 2016
## SUMMARY:
On Thursday 9 June 2016, the Google Cloud Console was unavailable for a duration of 91 minutes, with significant performance degradation in the preceding half hour. Although this did not affect user resources running on the Google Cloud Platform, we appreciate that many of our customers rely on the Cloud Console to manage those resources, and we apologize to everyone who was affected by the incident. This report is to explain to our customers what went wrong, and what we are doing to make sure that it does not happen again.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 9 June 2016 from 20:52 to 22:23 PDT, the Google Cloud Console was unavailable. Users who attempted to connect to the Cloud Console observed high latency and HTTP server errors. Many users also observed increasing latency and error rates during the half hour before the incident.
Google Cloud Platform resources were unaffected by the incident and continued to run normally. All Cloud Platform resource management APIs remained available, allowing Cloud Platform resources to be managed via the Google Cloud SDK or other tools.
## ROOT CAUSE:
The Google Cloud Console runs on Google App Engine, where it uses internal functionality that is not used by customer applications. Google App Engine version 1.9.39 introduced a bug in one internal function which affected Google Cloud Console instances, but not customer-owned applications, and thus escaped detection during testing and during initial rollout. Once enough instances of Google Cloud Console had been switched to 1.9.39, the console was unavailable and internal monitoring alerted the engineering team, who restored service by starting additional Google Cloud Console instances on 1.9.38.
During the entire incident, customer-owned applications were not affected and continued to operate normally.
To prevent a future recurrence, Google engineers are augmenting the testing and rollout monitoring to detect low error rates on internal functionality, complementing the existing monitoring for customer applications.
REMEDIATION AND PREVENTION:
When the issue was provisionally identified as a specific interaction between Google App Engine version 1.9.39 and the Cloud Console, App Engine engineers brought up capacity running the previous App Engine version and transferred the Cloud Console to it, restoring service at 22:23 PDT.
The low-level bug that triggered the error has been identified and fixed.
Google engineers are increasing the fidelity of the rollout monitoring framework to detect error signatures that suggest negative interactions of individual apps with a new App Engine release, even the signatures are invisible in global App Engine performance statistics.
We apologize again for the inconvenience this issue caused our customers.

# [developers/console/19001](https://status.cloud.google.com/incident/developers/console/19001)
16:55 Mar 14, 2019
## ISSUE SUMMARY:
On Monday, 11 March 2019, Google Cloud Console was unavailable for a duration of 3 hours and 54 minutes. Although, Google Cloud Platform resources remained unaffected, we understand that a majority of our customers rely on Cloud Console to manage their cloud resources and we sincerely apologize to everyone who was affected by the incident. The issue also affected Firebase console and IAM service account activations.
## DETAILED DESCRIPTION OF IMPACT:
On Monday, 11 March 2019, from 09:26 to 13:20 US/Pacific, Cloud Console was unavailable. Users were unable to access and manage their GCP resources using Cloud Console. All Google Cloud Platform resources continued to function and were accessible using the gcloud CLI, and the Cloud Console iOS and Android apps. From 14:10 to 15:37 US/Pacific, for a duration of 1 hour 27 minutes, Firebase Console and IAM service account activation were also unavailable to users.
## ROOT CAUSE:
Most Google services use a quota system for rate limiting user requests. The quota system implements a variant of the classic token bucket algorithm [1].
The issue was triggered when a code change in the most recent release of the quota system introduced a bug, causing a fallback to significantly smaller, default quota limits,  resulting in user requests being denied.
While the Cloud Console team mitigated the issue at 13:20 US/Pacifc, the underlying issue with the quota system started affecting Firebase Console and IAM service account activation beginning 14:10 US/Pacific until it was mitigated at 15:37 US/Pacific.
REMEDIATION AND PREVENTION
Cloud Console engineers were alerted at 09:31 US/Pacific and began investigation shortly after. The issue was mitigated at 13:20 US/Pacific when quota server engineers granted additional quota to Cloud Console while they continued to investigate the root cause. The issue was permanently mitigated when the offending change was rolled back.
In addition to fixing the underlying bug, we will be fixing the error in our default quota configuration. We will also be improving our automated alerts system to cover obviously erroneous quota denials.
We apologize again for the inconvenience caused by this issue to our customers.
[1] https://en.wikipedia.org/wiki/Token_bucket

# [developers/console/19003](https://status.cloud.google.com/incident/developers/console/19003)
09:51 May 10, 2019
## ISSUE SUMMARY:
On Thursday 2 May 2019, Google Cloud Console experienced a 40% error rate for all pageviews over a duration of 1 hour and 53 minutes. To all customers affected by this Cloud Console service degradation, we apologize. We are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Thursday 2 May 2019 from 07:10 to 09:03 US/Pacific the Google Cloud Console served 40% of all pageviews with a timeout error. Affected console sections include Compute Engine, Stackdriver, Kubernetes Engine, Cloud Storage, Firebase, App Engine, APIs, IAM, Cloud SQL, Dataflow, BigQuery and Billing.
## ROOT CAUSE:
The Google Cloud Console relies on many internal services to properly render individual user interface pages. The internal billing service is one of them, and is required to retrieve accurate state data for projects and accounts.
At 07:09 US/Pacific, a service unrelated to the Cloud Console began to send a large amount of traffic to the internal billing service. The additional load caused time-out and failure of individual requests including those from Google Cloud Console. This led to the Cloud Console serving timeout errors to customers when the underlying requests to the billing service failed.
REMEDIATION AND PREVENTION
Cloud Billing engineers were automatically alerted to the issue at 07:15 US/Pacific and Cloud Console engineers were alerted at 07:21. Both teams worked together to investigate the issue and once the root cause was identified, pursued two mitigation strategies. First, we increased the resources for the internal billing service in an attempt to handle the additional load. In parallel, we worked to identify the source of the extraneous traffic and then stop it from reaching the service. Once the traffic source was identified, mitigation was put in place and traffic to the internal billing service began to decrease at 08:40. The service fully recovered at 09:03.
In order to reduce the chance of recurrence we are taking the following actions. We will implement improved caching strategies in the Cloud Console to reduce unnecessary load and reliance on the internal billing service. The load shedding response of the billing service will be improved to better handle sudden spikes in load and to allow for quicker recovery should it be needed. Additionally, we will improve monitoring for the internal billing service to more precisely identify which part of the system is running into limits. Finally, we are reviewing dependencies in the serving path for all pages in the Cloud Console to ensure that necessary internal requests are handled gracefully in the event of failure.

# [google/stackdriver/18007](https://status.cloud.google.com/incident/google/stackdriver/18007)
13:03 May 24, 2018
## ISSUE SUMMARY:
On Sunday, 20 May 2018 for 4 hours and 25 minutes, approximately 6% of Stackdriver Logging logs experienced a median ingest latency of 90 minutes. To our Stackdriver Logging customers whose operations monitoring was impacted during this outage, we apologize. We have conducted an internal investigation and are taking steps to ensure this doesnât happen again.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday, 20 May 2018 from 18:40 to 23:05 Pacific Time, 6% of logs ingested by Stackdriver Logging experienced log event ingest latency of up to 2 hours 30 minutes, with a median latency of 90 minutes. Customers requesting log events within the latency window would receive empty responses. Logging export sinks were not affected.
## ROOT CAUSE:
Stackdriver Logging uses a pool of workers to persist ingested log events. On Wednesday, 20 May 2018 at 17:40, a load spike in the Stackdriver Logging storage subsystem caused 0.05% of persist calls made by the workers to time out. The workers would then retry persisting to the same address until reaching a retry timeout. While the workers were retrying, they were not persisting other log events. This resulted in multiple workers removed from the pool of available workers.
By 18:40, enough workers had been removed from the pool to reduce throughput below the level of incoming traffic, creating delays for 6% of logs.
REMEDIATION AND PREVENTION
After Google Engineering was paged, engineers isolated the issue to these timing out workers. At 20:35, engineers configured the workers to return timed out log events to queue and move on to a different log event after timeout. This allowed workers to catch up with ingest rate. At 23:02, the last delayed message was delivered.
We are taking the following steps to prevent the issue from happening again: we are modifying the workers to retry persists using alternate addresses to reduce the impact of persist timeouts; we are increasing the persist capacity of the storage subsystem to manage load spikes; we are modifying Stackdriver Logging workers to reduce their unavailability when the storage subsystem experiences higher latency.

# [google/stackdriver/19007](https://status.cloud.google.com/incident/google/stackdriver/19007)
15:38 Sep 27, 2019
## ISSUE SUMMARY:
On Tuesday 24 September, 2019, the following Google Cloud Platform services were partially impacted by an overload condition in an internal publish/subscribe messaging system which is a dependency of these products: App Engine, Compute Engine, Kubernetes Engine, Cloud Build, Cloud Composer, Cloud Dataflow, Cloud Dataproc, Cloud Firestore, Cloud Functions, Cloud DNS, Cloud Run, and Stackdriver Logging & Monitoring. Impact was limited to administrative operations for a number of these products, with existing workloads and instances not affected in most cases.
We apologize to those customers whose services were impacted during this incident; we are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 24 September, 2019 from 12:46 to 20:00 US/Pacific, Google Cloud Platform experienced a partial disruption to multiple services with their respective impacts detailed below:
App Engine
Google App Engine (GAE) create, update, and delete admin operations failed globally from 12:57 to 18:21 for a duration of 5 hours and 24 minutes. Affected customers may have seen error messages like âAPP_ERRORâ. Existing GAE workloads were unaffected.
Compute Engine
Google Compute Engine (GCE) instances failed to start in us-central1-a from 13:11 to 14:32 for a duration of 1 hour and 21 minutes, and GCE Internal DNS in us-central1, us-east1, and us-east4 experienced delays for newly created hostnames to become resolvable. Existing GCE instances and hostnames were unaffected.
Kubernetes Engine
Google Kubernetes Engine (GKE) experienced delayed resource metadata and inaccurate Stackdriver Monitoring for cluster metrics globally. Additionally, cluster creation operations failed in us-central1-a from 3:11 to 14:32 for a duration of 1 hour and 21 minutes due to its dependency on GCE instance creation. Existing GKE clusters were unaffected by the GCE instance creation failures.
Stackdriver Logging & Monitoring
Stackdriver Logging experienced delays of up to two hours for logging events generated globally. Exports were delayed by up to 3 hours and 30 minutes. Some user requests to write logs in us-central1 failed. Some logs-based metric monitoring charts displayed lower counts, and queries to Stackdriver Logging briefly experienced a period of 50% error rates. The impact to Stackdriver Logging & Monitoring took place from 12:54 to 18:45 for a total duration of 5 hours and 51 minutes.
Cloud Functions
Cloud Functions deployments failed globally from 12:57 to 18:21 and experienced peak error rates of 13% in us-east1 and 80% in us-central1 from 19:12 to 19:57 for a combined duration of 6 hours and 15 minutes. Existing Cloud Function deployments were unaffected.
Cloud Build
Cloud Build failed to update build status for GitHub App triggers from 12:54 to 16:00 for a duration of 3 hours and 6 minutes.
Cloud Composer
Cloud Composer environment creations failed globally from 13:25 to 18:05 for a duration of 4 hours and 40 minutes. Existing Cloud Composer clusters were unaffected.
Cloud Dataflow
Cloud Dataflow workers failed to start in us-central1-a from 13:11 to 14:32 for a duration of 1 hour and 21 minutes due to its dependency on Google Compute Engine instance creation. Affected jobs saw error messages like âStartup of the worker pool in zone us-central1-a failed to bring up any of the desired X workers. INTERNAL_ERROR: Internal error. Please try again or contact Google Support. (Code: '-473021768383484163')â. All other Cloud Dataflow regions and zones were unaffected.
Cloud Dataproc
Cloud Dataproc cluster creations failed in us-central1-a from 13:11 to 14:32 for a duration of 1 hour and 21 minutes due to its dependency on Google Compute Engine instance creation. All other Cloud Dataproc regions and zones were unaffected.
Cloud DNS
Cloud DNS in us-central1, us-east1, and us-east4 experienced delays for newly created or updated Private DNS records to become resolvable from 12:46 to 19:51 for a duration of 7 hours and 5 minutes.
Cloud Firestore
Cloud Firestore API was unable to be enabled (if not previously enabled) globally from 13:36 to 17:50 for a duration of 4 hours and 14 minutes.
Cloud Run
Cloud Run new deployments failed in the us-central1 region from 12:48 to 16:35 for a duration of 3 hours and 53 minutes. Existing Cloud Run workloads, and deployments in other regions were unaffected.
## ROOT CAUSE:
Google runs an internal publish/subscribe messaging system, which many services use to propagate state for control plane operations. That system is built using a replicated, high-availability key-value store, holding information about current lists of publishers, subscribers and topics, which all clients of the system need access to.
The outage was triggered when a routine software rollout of the key-value store in a single region restarted one of its tasks. Soon after, a network partition isolated other tasks, transferring load to a small number of replicas of the key-value store. As a defense-in-depth, clients of the key-value store are designed to continue working from existing, cached data when it is unavailable; unfortunately, an issue in a large number of clients caused them to fail and attempt to resynchronize state. The smaller number of key-value store replicas were unable to sustain the load of clients synchronizing state, causing those replicas to fail. The continued failures moved load around the available replicas of the key-value store, resulting in a degraded state of the interconnected components.
The failure of the key-value store, combined with the issue in the key-value store client, meant that publishers and subscribers in the impacted region were unable to correctly send and receive messages, causing the documented impact on dependent services.
REMEDIATION AND PREVENTION
Google engineers were automatically alerted to the incident at 12:56 US/Pacific and immediately began their investigation. As the situation began to show signs of cascading failures, the scope of the incident quickly became apparent and our specialized incident response team joined the investigation at 13:58 to address the problem. The early hours of the investigation were spent organizing, developing, and trialing various mitigation strategies. At 15:59 a potential root cause was identified and a configuration change submitted which increased the client synchronization delay allowed by the system, allowing clients to successfully complete their requests without timing out and reducing the overall load on the system. By 17:24, the change had fully propagated and the degraded components had returned to nominal performance.
In order to reduce the risk of recurrence, Google engineers configured the system to limit the number of tasks coordinating publishers and subscribers, which is a driver of load on the key-value store. The initial rollout of the constraint was faulty, and caused a more limited recurrence of problems at 19:00. This was quickly spotted and completely mitigated by 20:00, resolving the incident.
We would like to apologize for the length and severity of this incident. We have taken immediate steps to prevent recurrence of this incident and improve reliability in the future. In order to reduce the chance of a similar class of errors from occurring we are taking the following actions. We will revise provisioning of the key-value store to ensure that it is sufficiently resourced to handle sudden failover, and fix the issue in the key-value store client so that it continues to work from cached data, as designed, when the key-value store fails. We will also shard the data to reduce the scope of potential impact when the key-value store fails. Furthermore, we will be implementing automatic horizontal scaling of key-value store tasks to enable faster time to mitigation in the future. Finally, we will be improving our communication tooling to more effectively communicate multi-product outages and disruptions.
NOTE REGARDING CLOUD STATUS DASHBOARD COMMUNICATION
Incident communication was centralized on a single product - in this case Stackdriver - in order to provide a central location for customers to follow for updates. We realize this may have created the incorrect impression that Stackdriver was the root cause. We apologize for the miscommunication and will make changes to ensure that we communicate more clearly in the future.
SLA CREDITS
If you believe your paid application experienced an SLA violation as a result of this incident, please submit the SLA credit request: https://support.google.com/cloud/contact/cloud_platform_sla
A full list of all Google Cloud Platform Service Level Agreements can be found at: https://cloud.google.com/terms/sla/.

# [storage/16017](https://status.cloud.google.com/incident/storage/16017)
18:59 Oct 09, 2014
## SUMMARY:
On Wednesday 8 October 2014, some Google Cloud Storage users experienced increased error rates for 70 minutes. If you were affected by this issue we apologize.  Our goal is to provide you with a high level of reliability and availability, which we failed to meet in this situation.  We are taking immediate steps to improve Google Cloud Storageâs reliability and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 8 October 2014 from 14:15 to 15:30 PDT, 3% of requests to the Google Cloud Storage XML API and 2.9% of requests to the JSON API received an HTTP 500 or 503 response.  No increase in latency was observed during the incident.
## ROOT CAUSE:
On Wednesday 8 October 2014, two independent fiber cuts resulted in the loss of a terabit of network capacity between Google datacenters. The impact of this loss of capacity was increased due to coincident maintenance on a third fiber link. This resulted in packet loss on the remaining links due to saturation.
REMEDIATION AND PREVENTION:
The loss of network capacity and impacted network links were identified at 14:30 PDT by Google engineers who notified the fiber provider.  Google engineers then took action to route traffic away from the affected links to reduce congestion and quickly bring the link in maintenance back into service.  Error rates for Google Cloud Storage returned to baseline levels at 15:30 PDT.  The fiber repairs were finished on 9 October 2014 at 09:34.
To minimize impact in future incidents of this sort, we will increase the priority of Google Cloud Storage traffic on Google's production network so that it will be more resilient to loss of network capacity.

# [storage/16018](https://status.cloud.google.com/incident/storage/16018)
15:41 Oct 23, 2014
## SUMMARY:
On Wednesday 22 October 2014, some users of Google BigQuery, Google Cloud Storage and the Google Developers Console experienced elevated error rates for a period of 62 minutes. We apologize if your service or application was affected. We take these incidents extremely seriously and are taking immediate steps to ensure that this type of incident does not happen again.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 22 October 2014 from 14:30 to 15:32 PDT the following Google Cloud Platform services experienced elevated error rates: the Developers Console experienced a 96% error rate; BigQuery experienced a 45% error rate; and Cloud Storage experienced a 6.0% error rate for the XML API and a 3.4% error rate for the JSON API.
## ROOT CAUSE:
The incident occurred when Googleâs internal project metadata store experienced elevated latency, which was caused by an internal system writing to the metadata store at a higher rate than normal. BigQuery, Cloud Storage and the Developers Console frequently need to read project metadata in order to handle requests.
REMEDIATION AND PREVENTION:
Google engineers detected the incident at 14:36. We identified the root cause as the project metadata store at 14:58. At 15:06, we disabled the component of the metadata store that was responsible for the increased latency. The rollout of this fix was completed by 15:32.
In order to prevent future problems of this nature from happening again, we will fix the performance issue in the metadata store that caused its latency to increase when under higher load. For Cloud Storage and BigQuery, we will improve caching of project metadata so that a failure of the metadata store has less impact on the service. We will also make monitoring improvements to get earlier detection and faster diagnosis of problems with the metadata store.

# [storage/16020](https://status.cloud.google.com/incident/storage/16020)
09:54 Jan 30, 2015
## SUMMARY:
On Wednesday 28 January 2015, some API calls to BigQuery and Cloud Storage returned errors for a duration of 26 minutes. We apologize if your service or application was affected. We are working hard to avoid a recurrence of this type of issue.
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday 28 January 2015 from 17:01 to 17:27 PST, some API calls to BigQuery and Cloud Storage returned errors. The error rate for BigQuery was 11% during the period of the incident. The error rate for the Cloud Storage XML API was 6%. The error rate for the Cloud Storage JSON API was 12%. The Developers Console returned HTTP 500 errors for 41% of requests for a period of 11 minutes, from 17:01 to 17:12.
## ROOT CAUSE:
The incident resulted from releasing a bad configuration for an internal service, which caused processes to crash. Normally, Google âcanariesâ new releases, by upgrading a small number of servers and looking for problems before releasing the change everywhere. In this case, the canary process failed to operate correctly, causing a large number of processes to crash.
REMEDIATION AND PREVENTION:
Automated monitoring detected the issue and alerted our engineers at 17:02, one minute after the start of the incident. We began rolling back the release at 17:16. The roll back was complete by 17:27.
We are taking several actions to prevent a future recurrence of this type of incident. We have identified the issue that caused processes to crash, and are fixing the issue that caused the canary process to fail.

# [storage/16021](https://status.cloud.google.com/incident/storage/16021)
06:04 Mar 11, 2015
## SUMMARY:
On Monday March 9 2015, for a duration of 96 minutes, users of the Google Cloud Storage JSON API experienced elevated error rates. During the impacted period, 5% of all JSON API requests were erroneously denied with rate limiting and authorization errors. This affected all users of the JSON API, including App Engine applications, but did not affect users of the XML API.
## DETAILED DESCRIPTION OF IMPACT:
On March 9 2015 from 17:49 PDT to 19:25 Google Cloud Storage JSON API clients experienced a period of elevated error rates. During this period, 5% of requests to the Google Cloud Storage JSON API experienced Rate Limit Exceeded errors. The error rate peaked at 18% at 19:22.
## ROOT CAUSE:
A single large project generated a spike in requests to the Cloud Storage JSON API. This triggered a monitoring system to alert Google engineers who, following standard procedures, severely limited the projectâs API access rate to prevent impact on other projects.
The projectâs clients responded to the resulting Rate Limit Exceeded errors with retry behavior causing an even larger traffic spike that, at its peak, was an order of magnitude greater than normal traffic rates. Because the service was not provisioned for this spike in traffic, it responded to this flood of requests by denying many of them with Rate Limit Exceeded errors, including a portion of traffic from other projects.
REMEDIATION AND PREVENTION:
Shortly after identifying the source of the traffic, Google engineers contacted the owners of the project and worked with them to analyze and mitigate the traffic surge. The limitations placed on the project protected the majority of traffic. Once Google engineers confirmed there was no more risk from the project, they removed the limit, and the remaining impact was resolved.
To prevent this class of issues in the future, Google engineers will implement a traffic control mechanism that is more robust in the face of client retry amplification. Additionally, Google engineers are creating more detailed monitoring systems that provide clearer, quicker insight into the source of traffic spikes of this nature. Finally, Google engineers are updating and refining standard procedures to rapidly and effectively respond to extreme situations of this nature.

# [storage/16023](https://status.cloud.google.com/incident/storage/16023)
01:16 May 08, 2015
## SUMMARY:
On Tuesday 5 May 2015 and Wednesday 6 May 2015, Google Cloud Storage (GCS) experienced elevated request latency and error rates for a total duration of 43 minutes during two separate periods. We understand how important uptime and latency are to you and we apologize for this disruption. We are using the lessons from this incident to achieve a higher level of service in the future.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 5 May 2015 from 12:26 to 12:48 PDT requests to GCS returned with elevated latency and error rates. Averaged over the incident, 33% of requests returned error code 500 or 503. At 12:34 the error rate peaked at 42% of requests. Median latency for successful requests increased by 29%.
On Wednesday 6 May from 19:25 to 19:41 PDT, and for two minutes at 19:46 and three minutes at 19:52, the same symptoms were seen with a 64% average error rate and 55% increase in median latency.
## ROOT CAUSE:
At 12:25 on 5 May 2015 GCS received an extremely high rate of requests to a small set of GCS objects, causing high load and queuing on a single metadata database shard. This load caused a fraction of unrelated GCS requests to be queued as well, resulting in latency and timeouts visible to other GCS users.
At 19:25 on 6 May 2015 GCS received a second round of unusual load to a different set of objects, causing a recurrence of the same issue.
REMEDIATION AND PREVENTION:
In both incidents, Google engineers identified the set of GCS objects affected and increased localized caching to increase capacity.  The Google support team also contacted the project generating the load and worked with them to reduce their demand.
In addition to these tactical fixes, Google engineers will enable service-wide caching for the affected GCS components. Google engineers are also working on other steps to improve service isolation between unrelated GCS objects and projects.

# [storage/16024](https://status.cloud.google.com/incident/storage/16024)
04:11 May 18, 2015
## SUMMARY:
On Friday 15 May 2015, uploads to Google Cloud Storage experienced increased latency and error rates for a duration of 1 hour 38 minutes. If your service or application was affected, we apologize. We understand that many services and applications rely on consistent performance when uploading objects to our service and we failed to uphold that level of performance.  We are taking immediate actions to ensure this issue does not happen again.
## DETAILED DESCRIPTION OF IMPACT:
On Friday 15 May 2015 from 03:35 to 05:13 PDT, uploads to Google Cloud Storage either failed or took longer than expected. During the incident, 6% of all POST requests globally returned error code 503 between 03:35 and 03:43, and the error rate remained at >0.5% until 05:13. Google Cloud Storage is a highly distributed system; one of Google's US datacenters was the focus of much of the impact, with an error rate peaking at over 40%. Median latency for successful requests increased 16%, compared to typical levels, while latency at the 90th and 99th percentiles increased 29% and 63% respectively.
## ROOT CAUSE:
A periodic replication job, run automatically against Google Cloud Storage's underlying storage system, increased load and reduced available resources for processing new uploads. As a result, latency increased and uploads to GCS either continued to wait for completion or failed.
REMEDIATION AND PREVENTION:
Google engineers were alerted to increased latency in one of the datacenters responsible for processing uploads at 03:12 PDT and redirected upload traffic to several other datacenters to distribute the load. When it was evident this redirection had not alleviated the increase in latency, engineers began to provision additional capacity while continuing to investigate the underlying root cause. When the replication job was identified as the source of the increased load, Google engineers reduced the rate of replication and service was restored.
In the short term, Google engineers will be adding additional monitoring to the underlying storage layer to better identify problematic system load conditions as well as the tasks responsible. In the longer term, Google engineers will be isolating the impact the replication job can have on the latency and performance of other services.

# [storage/16025](https://status.cloud.google.com/incident/storage/16025)
02:11 Jun 11, 2015
## SUMMARY:
On Tuesday 9 June 2015 Google Cloud Storage served an elevated error rate and latency for a duration of 1 hour 40 minutes. If your service or application was affected, we apologize. We understand that many services and applications rely on consistent performance of our service and we failed to uphold that level of performance. We are taking immediate actions to ensure this issue does not happen again.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 9 June 2015 from 15:29 to 17:09 PDT, an average of 52.7% of the global requests to Cloud Storage resulted in HTTP 500 or 503 responses. The impact was most pronounced for GCS requests in the US with 55% average error rate, while requests to GCS in Europe and Asia resulted in 25% and 1% failures, respectively.
## ROOT CAUSE:
The incident resulted from a change in the default behavior of a dependency of Cloud Storage that was included in a new GCS server release. At scale, the change led to pathological retry behavior which eventually caused increased latency, led to request timeouts, threadpool saturation and an increased error rate for the service. Google follows a canary process for all new releases, by upgrading a small number of servers and looking for problems before releasing the change everywhere in a gradual fashion. In this case the traffic served from those canary servers was not sufficient to expose the issue.
REMEDIATION AND PREVENTION:
Automated monitoring detected increased latency for Cloud Storage requests in one datacenter at 15:44. In an attempt to mitigate the problem and allow the troubleshooting of the underlying issue to continue, engineers increased resources to several backend systems that were exhibiting hotspotting problems which resulted in a small improvement. When it was evident that this was related to a behavior change in one of the libraries for a dependent system, Google Engineers made the necessary production adjustments to stabilize the system by quickly disabling the pathological retry behavior.
To prevent similar issues from happening in the future we're making a number of changes: Cloud Storage release tools will be upgraded to allow for quicker rollbacks, risky changes will be released through an experimental traffic framework allowing for more precise canarying, and our outage response procedures will default to rolling back new releases more quickly as a default mitigation for all incidents.

# [storage/16027](https://status.cloud.google.com/incident/storage/16027)
23:10 Aug 10, 2015
## SUMMARY:
On Saturday 8 August 2015, Google Cloud Storage served an elevated error rate for a duration of 139 minutes. If your service or application was affected, we apologize.  We have taken an initial set of actions to prevent recurrence of the problem, and have a larger set of changes which will provide defense in depth currently under review by the engineering teams.
## DETAILED DESCRIPTION OF IMPACT:
On Saturday 8 August 2015 from 20:21 to 22:40 PDT, Google Cloud Storage returned a high rate of error responses to queries. The average error rate during this time was 28.4%, with an initial peak of 47% at 20:27. Error levels gradually decreased subsequently, with intermediate periods of normal operation from 21:46-21:54 and 22:04-22:10. Usage was equally affected across the Google Cloud Storage XML and JSON APIs.
## ROOT CAUSE:
The elevated GCS error rate was induced by a large increase in traffic compared to normal levels.  The traffic surge was exacerbated by retries from software clients receiving errors.  The GCS errors were principally served to the sources which were generating the unusual traffic levels, but a fraction of the errors were served to other users as well.
REMEDIATION AND PREVENTION:
Google engineers were alerted to the elevated error rate by automated monitoring, and took steps to both reduce the impact and to increase capacity to mitigate the duration and severity of the incident for GCS users.  In parallel, Googleâs support team contacted the system owners which were generating the bulk of unexpected traffic, and helped them reduce their demand.  The combination of these two actions resolved the incident.
To prevent a potential future recurrence, Googleâs engineering team have made or are making a number of changes to GCS, including:

Adding traffic rate âcollaringâ to prevent unexpected surges in demand from exceeding sustainable levels;
Adding or improving caching at multiple levels in order to increase capacity, and increase resilience to repetitive queries;
Changing RPC queuing behavior in GCS to provide more capacity and more graceful handling of overload.


# [storage/16029](https://status.cloud.google.com/incident/storage/16029)
15:30 Aug 28, 2015
## SUMMARY:
On Wednesday 26 August 2015, requests to Signed URLs [1] on Google Cloud Storage (GCS) returned errors for an extended period of time, affecting approximately 18% of projects using the Signed URLs feature. We apologize to our customers who were affected by this issue. We have identified and fixed the root causes of the incident, and we are putting measures in place to keep similar issues from occurring in future.
[1] https://cloud.google.com/storage/docs/access-control#Signed-URLs
## DETAILED DESCRIPTION OF IMPACT:
On Wednesday August 26th 2015 at 07:26 PDT, approximately 18% of projects sending requests to GCS Signed URLs started receiving HTTP 500 and 503 responses. The majority of the errors occurred from 07:25 to 10:34 PDT. From 10:34 the number of affected projects decreased, and by 11:25 PDT fewer than 2% of Signed URL requests were receiving errors. A small number of projects encountered continued errors until remediation was completed at 20:38.
There was no disruption to any GCS functionality that did not involve Signed URLs.
## ROOT CAUSE:
GCS Signed URLs are cryptographically signed by the owner of the stored data, using the private key of a Google Cloud Platform service account. The private key is known only to the owner, but the corresponding public key is retained by Google and used to verify the URL signatures.
Within Google, similar service accounts are used for many internal authentication purposes. (For example, these accounts include the default service account which internally represents the customer's Cloud Platform project.) For these service accounts, Google retains both the public and the private key. These keypairs have a short lifetime and are frequently regenerated.
All keys are managed in a central, strongly hardened security module. As part of an effort to simplify the key management system, prior to the incident, a configuration change was pushed which mistakenly caused the security module to consider customers' service accounts as candidates for automatic keypair management. This change was later rolled back, removing the service accounts from automatic management, but some customers' service accounts had already received new keypairs with finite lifetimes. Accounts with heavy Signed URL usage were more likely to be affected.
On 07:25 PDT on Wednesday 26 August, the lifetimes of the temporary keypairs for affected accounts began to expire. Since the expired keypairs were not automatically removed as the service account were no longer under automatic management, it's presence was treated as an error by the Signed URL verification process, causing all Signed URL requests for the service account to fail.
At no time during this incident were any keys at risk and they remain safe and secure. No action is required by customers.
REMEDIATION AND PREVENTION
Automated monitoring signalled the issue at 07:33. Google engineers identified the need to remove the expired keys, which required manual access to the security module.  This is protected by multiple security procedures, by design, so it required several escalations to get the correct people. Access was gained at 10:34 PDT, and thereafter service was progressively restored as each service account was reactivated by removing its expired keys.
To eliminate the immediate cause of the issue, Google engineers are modifying the URL signature verifier to be more robust when it encounters expired keys.
To avoid various related classes of errors, Google engineers are increasing the testing performed on configuration changes for the security system, both to strengthen consistency and to ensure that configuration changes do not induce unexpected side effects.
In case of other future issues with the security module, Google engineers are streamlining internal escalation procedures to improve response times, and upgrading tools for more efficient key administration.

# [storage/17002](https://status.cloud.google.com/incident/storage/17002)
14:27 Jul 14, 2017
## ISSUE SUMMARY:
On Thursday, 6 July 2017, requests to Google Cloud Storage (GCS) JSON API experienced elevated error rates for a period of 3 hours and 15 minutes. The GCS XML API was not affected.
Requests to www.googleapis.com that used OAuth2 credentials experienced elevated error rates for 29 minutes, which directly caused higher failure rates for other products, including Firebase and Google Cloud Functions.
If your service or applicationâs was affected by this issue, we sincerely apologize. We understand the importance of reliable APIs and are currently taking steps to prevent future recurrences of this issue.
## DETAILED DESCRIPTION OF IMPACT:
Starting on Thursday, 6 July 2017 at 15:15 PDT and continuing for 60 minutes, requests to the GCS JSON API experienced elevated error rates that peaked at 40%. At 16:15 error rates returned to normal. Then from 16:51 to 18:30, the JSON API request error rate peaked at a 97%.
Requests to www.googleapis.com that used OAuth2 credentials experienced an 82% error rate from 15:35 to 16:04, which many services rely on for tokens, userinfo and token information.
Firebase Hosting and Functions was impacted from 15:15 to 18:30, during which deployment error rates reached a 99% failure rate due to a joint dependence on GCS uploads and OAuth2.
Google Cloud Functions (GCF) deployments experienced a 1.2% failure rate when attempting a deployment.
Other services that rely on Google APIs experienced <1% error rates.
Most HTTP responses returned to customers were of type â503 Service Unavailable.â
The issue was resolved at 18:31 when normal service was restored.
## ROOT CAUSE:
A low-level software defect in an internal API service that handles GCS JSON requests caused infrequent memory-related process terminations. These process terminations increased as a result of a large volume in requests to the GCS Transfer Service, which uses the same internal API service as the GCS JSON API. This caused an increased rate of 503 responses for GCS JSON API requests for 3.25 hours.
While attempting to fix the latency, the traffic for GCS JSON requests was isolated from other API traffic. 
After the traffic was isolated, attempts to mitigate the problem caused the error rate to increase to 97%.  The problem was finally fixed when a further configuration change fixed the process terminations.
REMEDIATION AND PREVENTION
Google engineers were paged by automated monitoring, and began troubleshooting before the issue symptoms were visible to customers at 15:15. Initially a configuration issue caused traffic to be moved away from dedicated clusters that were available to isolate the root cause. However, engineers immediately detected the high error rate and moved traffic to the dedicated clusters. This decreased the error rates experienced by customers.  A follow-on configuration change pushed by Google engineers stopped new process terminations, which allowed the backends to heal, and normal service was restored.
To prevent further issues of this type, we are re-examining the best way to mitigate the impact of memory-related process terminations, so that they do not impact serving traffic. We are also investigating methods of isolating problematic traffic patterns to subsets of backends, to avoid widespread failures.
We apologize for the impact that this incident had on your services, deployments, and API calls.  We will fix the underlying issue that started the initial issue, and take this opportunity to make other changes to prevent this issue from occurring again.

# [storage/17005](https://status.cloud.google.com/incident/storage/17005)
12:49 Oct 19, 2017
## ISSUE SUMMARY:
Starting Thursday 12 October 2017, Google Cloud Storage clients located in the Northeast of North America experienced up to a 10% error rate for a duration of 21 hours and 35 minutes when fetching objects stored in multi-regional buckets in the US.
We apologize for the impact of this incident on your application or service. The reliability of our service is a top priority and we understand that we need to do better to ensure that incidents of this type do not recur.
## DETAILED DESCRIPTION OF IMPACT:
Between Thursday 12 October 2017 12:47 PDT and Friday 13 October 2017 10:12 PDT, Google Cloud Storage clients located in the Northeast of North America experienced up to a 10% rate of 503 errors and elevated latency. Some users experienced higher error rates for brief periods. This incident only impacted requests to fetch objects stored in multi-regional buckets in the US; clients were able to mitigate impact by retrying. The percentage of total global requests to Cloud Storage that experienced errors was 0.03%.
## ROOT CAUSE:
Google ensures balanced use of its internal networks by throttling outbound traffic at the source host in the event of congestion. This incident was caused by a bug in an earlier version of the job that reads Cloud Storage objects from disk and streams data to clients. Under high traffic conditions, the bug caused these jobs to incorrectly throttle outbound network traffic even though the network was not congested.
Google had previously identified this bug and was in the process of rolling out a fix to all Google datacenters. At the time of the incident, Cloud Storage jobs in a datacenter in Northeast North America that serves requests to some Canadian and US clients had not yet received the fix. This datacenter is not a location for customer buckets (https://cloud.google.com/storage/docs/bucket-locations), but objects in multi-regional buckets can be served from instances running in this datacenter in order to optimize latency for clients.
REMEDIATION AND PREVENTION
The incident was first reported by a customer to Google on Thursday 12 October 14:59 PDT. Google engineers determined root cause on Friday 13 October 09:47 PDT. We redirected Cloud Storage traffic away from the impacted region at 10:08 and the incident was resolved at 10:12.
We have now rolled out the bug fix to all regions. We will also add external monitoring probes for all regional points of presence so that we can more quickly detect issues of this type.

# [storage/18003](https://status.cloud.google.com/incident/storage/18003)
20:00 Sep 07, 2018
## ISSUE SUMMARY:
On Tuesday 4 September 2018, Google Cloud Storage experienced 1.1% error rates and increased 99th percentile latency for US multiregion buckets for a duration of 5 hours 38 minutes. After that time some customers experienced 0.1% error rates which returned to normal progressively over the subsequent 4 hours. To our Google Cloud Storage customers whose businesses were impacted during this incident, we sincerely apologize; this is not the level of tail-end latency and reliability we strive to offer you. We are taking immediate steps to improve the platformâs performance and availability.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 4 September 2018 from 02:55 to 08:33 PDT, customers with buckets located in the US multiregion experienced a 1.066% error rate and 4.9x increased 99th percentile latency, with the peak effect occurring between 05:00 PDT and 07:30 PDT for write-heavy workloads. At 08:33 PDT 99th percentile latency decreased to 1.4x normal levels and error rates decreased, initially to 0.146% and then subsequently to nominal levels by 12:50 PDT.
## ROOT CAUSE:
At the beginning of August, Google Cloud Storage deployed a new feature which among other things prefetched and cached the location of some internal metadata. On Monday 3rd September 18:45 PDT, a change in the underlying metadata storage system resulted in increased load to that subsystem, which eventually invalidated some cached metadata for US multiregion buckets. This meant that requests for that metadata experienced increased latency, or returned an error if the backend RPC timed out. This additional load on metadata lookups led to elevated error rates and latency as described above.
REMEDIATION AND PREVENTION
Google Cloud Storage SREs were alerted automatically once error rates had risen materially above nominal levels. Additional SRE teams were involved as soon as the metadata storage system was identified as a likely root cause of the incident. In order to mitigate the incident, the keyspace that was suffering degraded performance needed to be identified and isolated so that it could be given additional resources. This work completed by the 4th September 08:33 PDT. In parallel, Google Cloud Storage SREs pursued the source of additional load on the metadata storage system and traced it to cache invalidations.
In order to prevent this type of incident from occurring again in the future, we will expand our load testing to ensure that performance degradations are detected prior to reaching production. We will improve our monitoring diagnostics to ensure that we more rapidly pinpoint the source of performance degradation. The metadata prefetching algorithm will be changed to introduce randomness and further reduce the chance of creating excessive load on the underlying storage system. Finally, we plan to enhance the storage system to reduce the time needed to identify, isolate, and mitigate load concentration such as that resulting from cache invalidations.

# [storage/18005](https://status.cloud.google.com/incident/storage/18005)
09:53 Dec 28, 2018
## ISSUE SUMMARY:
On Friday 21 December 2018, customers deploying App Engine apps, deploying in Cloud Functions, reading from Google Cloud Storage (GCS), or using Cloud Build experienced increased latency and elevated error rates ranging from 1.6% to 18% for a period of 3 hours, 41 minutes.
We understand that these services are critical to our customers and sincerely apologize for the disruption caused by this incident; this is not the level of quality and reliability that we strive to offer you. We have several engineering efforts now under way to prevent a recurrence of this sort of problem; they are described in detail below.
## DETAILED DESCRIPTION OF IMPACT:
On Friday 21 December 2018, from 08:01 to 11:43 PST, Google Cloud Storage reads, App Engine deployments, Cloud Functions deployments, and Cloud Build experienced a disruption due to increased latency and 5xx errors while reading from Google Cloud Storage. The peak error rate for GCS reads was 1.6% in US multi-region. Writes were not impacted, as the impacted metadata store is not utilized on writes.
Elevated deployment errors for App Engine Apps in all regions averaged 8% during the incident period. In Cloud Build, a 14% INTERNAL_ERROR rate and 18% TIMEOUT error rate occurred at peak. The aggregated average deployment failure rate of 4.6% for Cloud Functions occurred in us-central1, us-east1, europe-west1, and asia-northeast1.
## ROOT CAUSE:
Impact began when increased load on one of GCS's metadata stores resulted in request queuing, which in turn created an uneven distribution of service load.
The additional load was created by a partially-deployed new feature. A routine maintenance operation in combination with this new feature resulted in an unexpected increase in the load on the metadata store. This increase in load affected read workloads due to increased request latency to the metadata store.
In some cases, this latency exceeded the timeout threshold, causing an average of 0.6% of requests to fail in the US multi-region for the duration of the incident.
REMEDIATION AND PREVENTION
Google engineers were automatically alerted to the increased error rate at 08:22 PST. Since the issue involved multiple backend systems, multiple teams at Google were involved in the investigation and narrowed down the issue to the newly-deployed feature. The latency and error rate began to subside as Google Engineers initiated the rollback of the new feature. The issue was fully mitigated at 11:43 PST when the rollback finished, at which point the impacted GCP services recovered completely.
In addition to updating the impacting feature to prevent this type of increased load, we will update the rollout workflow to stress feature limits before rollout.  To improve time to resolution of issues in the metadata store, we are implementing additional instrumentation to the requests made of the subsystem.

# [storage/19001](https://status.cloud.google.com/incident/storage/19001)
06:43 Feb 21, 2019
## ISSUE SUMMARY:
Google Cloud Storage experienced elevated error rates averaging 10% across the European multi-region for GET, PUT, and DELETE requests. Google Engineering fully mitigated this incident at 10:17 on Feb 5, 2019.  We will conduct an internal investigation of this issue and make appropriate improvements to our systems to help prevent or minimize future recurrence.

# [storage/19002](https://status.cloud.google.com/incident/storage/19002)
11:09 Mar 14, 2019
## ISSUE SUMMARY:
On Tuesday 12 March 2019, Google's internal blob storage service experienced a service disruption for a duration of 4 hours and 10 minutes. We apologize to customers whose service or application was impacted by this incident. We know that our customers depend on Google Cloud Platform services and we are taking immediate steps to improve our availability and prevent outages of this type from recurring.
## DETAILED DESCRIPTION OF IMPACT:
On Tuesday 12 March 2019 from 18:40 to 22:50 PDT, Google's internal blob (large data object) storage service experienced elevated error rates, averaging 20% error rates with a short peak of 31% errors during the incident. User-visible Google services including Gmail, Photos, and Google Drive, which make use of the blob storage service also saw elevated error rates, although (as was the case with GCS) the user impact was greatly reduced by caching and redundancy built into those services. There will be a separate incident report for non-GCP services affected by this incident.
The Google Cloud Platform services that experienced the most significant customer impact were the following:
Google Cloud Storage experienced elevated long tail latency and an average error rate of 4.8%. All bucket locations and storage classes were impacted. GCP services that depend on Cloud Storage were also impacted.
Stackdriver Monitoring experienced up to 5% errors retrieving historical time series data. Recent time series data was available. Alerting was not impacted.
App Engine's Blobstore API experienced elevated latency and an error rate that peaked at 21% for fetching blob data. App Engine deployments experienced elevated errors that peaked at 90%. Serving of static files from App Engine also experienced elevated errors.
## ROOT CAUSE:
On Monday 11 March 2019, Google SREs were alerted to a significant increase in storage resources for metadata used by the internal blob service. On Tuesday 12 March, to reduce resource usage, SREs made a configuration change which had a side effect of overloading a key part of the system for looking up the location of blob data. The increased load eventually lead to a cascading failure.
REMEDIATION AND PREVENTION
SREs were alerted to the service disruption at 18:56 PDT and immediately stopped the job that was making configuration changes. In order to recover from the cascading failure, SREs manually reduced traffic levels to the blob service to allow tasks to start up without crashing due to high load.
In order to prevent service disruptions of this type, we will be improving the isolation between regions of the storage service so that failures are less likely to have global impact. We will be improving our ability to more quickly provision resources in order to recover from a cascading failure triggered by high load. We will make software measures to prevent any configuration changes that cause overloading of key parts of the system. We will improve load shedding behavior of the metadata storage system so that it degrades gracefully under overload.

# [support/19002](https://status.cloud.google.com/incident/support/19002)
14:55 May 31, 2019
## ISSUE SUMMARY:
On Friday 17 May, 2019, Google Cloud Support experienced case creation and read issues for a duration of 4 hours. We sincerely apologize to our customers for the difficulties and delays in communicating with Google Cloud Support during this time.
## DETAILED DESCRIPTION OF IMPACT:
On Friday 17 May, 2019 from 10:08 to 14:07 US/Pacific, both Google Cloud Support and our customers were unable to view, create, and modify Support cases, utilize Chat Support, or view known issues via the Google Cloud Support Center (GCSC) and the Cloud Console. Phone support was also unavailable from 10:08 to 14:26.
## ROOT CAUSE:
A critical external dependency for Google Cloud Support encountered an issue resulting in service unavailability, which impacted both Googleâs and Google Cloud Platform customersâ ability to use the service. This impacted case creation for chat, phone, and email cases, which all rely on the external dependency to reference customer data and route to the correct channel. Unfortunately, our tooling also did not allow for an automated mitigation.
REMEDIATION AND PREVENTION
Googleâs engineers were alerted to the problem at 10:26 and escalated immediately. Once the nature and scope of the situation became clear, Cloud Support identified customer communication options through secondary channels. Customers were able to file cases through the backup âContact Supportâ mechanism that was automatically available in the Google Cloud Support Center (GCSC). All cases reported through the backup mechanism were routed internally to the appropriate Support Engineers.
We will refactor Cloud Supportâs Business Continuity Plan to account for issues of this nature, to ensure that:
- Existing cases can continue to be viewed and updated
- Chat Support will be available
- Phone support will be available

