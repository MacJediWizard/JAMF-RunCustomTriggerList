<h1><b>JAMF-RunCustomTriggerList</b></h1>

This is a very small Python script that can run a set of comma separated custom triggers in JAMF

This allowes you to reuse policies with custom triggere but not have to maintain more than one policy.

<hr>
<h3><b>Set-Up</b></h3>

The script is set up in JAMF under Settings --> Computer Management --> Scripts. In your Options section you set up Parameter 4 with the following text: "Comma Separated Custom Trigger List. (ex. trigger1, trigger2, trigger3)". Save and then use in your policies.

