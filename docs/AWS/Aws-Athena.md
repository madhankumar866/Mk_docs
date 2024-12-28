# Amazon  Athena

#################################################################################################
To count number of request url path per ip's
SELECT DISTINCT client_ip,
        request_url,
         count() AS count
FROM alb_logs
WHERE parse_datetime(time,'yyyy-MM-dd''T''HH:mm:ss.SSSSSS''Z')
    BETWEEN parse_datetime('2021-09-08-00:00:00','yyyy-MM-dd-HH:mm:ss')
        AND parse_datetime('2021-09-08-23:59:00','yyyy-MM-dd-HH:mm:ss')
GROUP BY  client_ip,request_url
ORDER BY  count() DESC
#################################################################################################


WITH dataset as
(
SELECT action as waf_action,
terminatingRuleType waf_rule_type,
terminatingruleid waf_rule_id,timestamp,
httprequest.clientip,
httprequest.country,
headeritems AS header,
httprequest.uri,
httprequest.args
FROM "shyaway_logs"."waf_global_alb_logs" waf
CROSS JOIN UNNEST(httprequest.headers) AS t(headeritems)
)
select count(*),waf_action, waf_rule_type,waf_rule_id, clientip, country, header.value, uri, args
from dataset
WHERE waf_action='BLOCK' AND timestamp between 1606483800000 and 1606548600000
GROUP BY waf_action,waf_rule_id,waf_rule_type,clientip,country,header.value, uri,args


#####################################################################################################################

WITH dataset as
(
SELECT action as waf_action,
terminatingRuleType waf_rule_type,
terminatingruleid test,
httprequest.clientip,
httprequest.country,
headeritems AS header,
httprequest.uri,
httprequest.args
FROM "shyaway_logs"."waf_global_alb_logs" waf
CROSS JOIN UNNEST(httprequest.headers) AS t(headeritems)
)
select waf_action, waf_rule_type,test, clientip, country, header.value, uri, args
from dataset
where header.name='user-agent'  and header.value='facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)' and waf_action='BLOCK' limit 10



#####################################################################################################################


SELECT COUNT(*) AS
count,httpRequest.country,
terminatingruleid,
httprequest.clientip,
action,
httprequest.uri,timestamp
FROM shyaway_waf_cdn_global_logs
WHERE action='BLOCK'
GROUP BY timestamp,httpRequest.country,terminatingruleid, httprequest.clientip, httprequest.uri, action
ORDER BY count DESC,timestamp DESC
LIMIT 1000;

#####################################################################################################################
SELECT *
FROM alb_logs
WHERE ("request_url" = 'https://www.shyaway.com:443/bra-online/?bra_offers=buy-2-get-3-free&sku=S28035-Red&utm_source=fblk1p&utm_medium=bra&utm_campaign=999off') limit 10

#####################################################################################################



################
CREATE OR REPLACE VIEW count-view-alb-logs AS 
SELECT
  "elb"
, "count"(*) "count"
FROM
  alb_logs
WHERE ("parse_datetime"("time", 'yyyy-MM-dd''T''HH:mm:ss.SSSSSS''Z') BETWEEN "parse_datetime"('2020-10-11-00:00:00', 'yyyy-MM-dd-HH:mm:ss') AND "parse_datetime"('2020-10-11-03:00:00', 'yyyy-MM-dd-HH:mm:ss'))
GROUP BY "elb"
LIMIT 100


#####################################################################################################################
SELECT elb,count(*) FROM "alb_logs" WHERE parse_datetime(time,'yyyy-MM-dd''T''HH:mm:ss.SSSSSS''Z')
    BETWEEN parse_datetime('2020-11-26-00:00:00','yyyy-MM-dd-HH:mm:ss')
        AND parse_datetime('2020-11-27-23:59:00','yyyy-MM-dd-HH:mm:ss')
GROUP BY elb
limit 10

#####################################################################################################################
SELECT COUNT(*) AS
count,elb_status_code,request_url,user_agent
FROM alb_logs
WHERE request_url='https://www.shyaway.com:443/bra-online/?bra_offers=buy-2-get-3-free&sku=S28035-Red&utm_source=fblk1p&utm_medium=bra&utm_campaign=999off'
GROUP BY elb_status_code,request_url,user_agent
ORDER BY count DESC
LIMIT 10;

#####################################################################################################################
SELECT COUNT(*) AS
count,elb_status_code,request_url,user_agent
FROM alb_logs
WHERE user_agent='facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)' AND elb_status_code='403'
GROUP BY request_url,elb_status_code,user_agent
ORDER BY count DESC
LIMIT 10;
#####################################################################################################################

SELECT COUNT(*) AS
count,httpRequest.country,
terminatingruleid,
httprequest.clientip,
action,
httprequest.uri,timestamp
FROM waf_global_alb_logs
WHERE action='BLOCK' AND timestamp between 1606503600000 and 1606863600000
GROUP BY timestamp,httpRequest.country,terminatingruleid, httprequest.clientip, httprequest.uri, action
ORDER BY count DESC,timestamp DESC
limit 10;

#####################################################################################################################

WITH dataset as
(
SELECT action as waf_action,
terminatingRuleType waf_rule_type,
terminatingruleid waf_rule_id,timestamp,
httprequest.clientip,
httprequest.country,
headeritems AS header,
httprequest.uri,
httprequest.args
FROM "shyaway_logs"."waf_global_alb_logs" waf
CROSS JOIN UNNEST(httprequest.headers) AS t(headeritems)
)
select count(*),waf_action, waf_rule_type,waf_rule_id, clientip, country, header.value, uri, args,timestamp,uri
from dataset
WHERE waf_action='BLOCK' AND timestamp between 1606503600000 and 1606863600000
GROUP BY waf_action,timestamp,waf_rule_id,waf_rule_type,clientip,country,header.value, uri,args,timestamp,uri
#####################################################################################################################
SELECT 	elb_status_code,client_ip,request_url,user_agent,
         count(*) AS count
FROM "shyaway_logs"."alb_log"
WHERE 	elb_status_code LIKE '%400%' AND parse_datetime(time,'yyyy-MM-dd''T''HH:mm:ss.SSSSSS''Z')
    BETWEEN parse_datetime('2021-01-04-01:01:00','yyyy-MM-dd-HH:mm:ss')
        AND parse_datetime('2021-01-04-23:59:00','yyyy-MM-dd-HH:mm:ss')
GROUP BY  	elb_status_code,client_ip,request_url,user_agent
ORDER BY  count DESC,request_url DESC,user_agent DESC

#####################################################################################################################
WITH dataset as
(
SELECT action as waf_action,
terminatingRuleType waf_rule_type,
terminatingruleid waf_rule_id,timestamp,
httprequest.clientip,
httprequest.country,
headeritems AS header,
httprequest.uri,
httprequest.args
FROM "shyaway_logs"."waf_global_alb_logs" waf
CROSS JOIN UNNEST(httprequest.headers) AS t(headeritems)
)
select count(*),waf_action, waf_rule_type,waf_rule_id, clientip, country, header.value, uri, args,timestamp,uri
from dataset
WHERE waf_action='BLOCK' AND timestamp > 1608187410000
GROUP BY waf_action,timestamp,wafj_rule_id,waf_rule_type,clientip,country,header.value, uri,args,uri

#####################################################################################################################