---
layout: page
title: Tutorial - Enable Single Sign On Authentication
description:  Enable Single Sign On Authentication
---

To support the ever growing amount of users on our platform and to improve the usability of their user management we added support for SSO. This will make it easier supporting large user-bases of CoScale both on-premise as on our SAAS platform.
We added support for organisations and teams. This makes it really easy to give (limited) access to a particular team on some of the CoScale applications for your organisation.

### 1. Click on your username, in the top right corner of your app

Select "My organisation" from the drop down.

<img src="{{ site.baseurl}}/gfx/tutorials/sso-authentication/01-click-username.png" alt="Click username" class="img-responsive" />

### 2. Click on "Enable SSO"

<img src="{{ site.baseurl}}/gfx/tutorials/sso-authentication/02-enable-sso.png" alt="Enable SSO" class="img-responsive" />

### 3. Fill in the required fields

* SSO Url
* Entity ID
* Certificate

<img src="{{ site.baseurl}}/gfx/tutorials/sso-authentication/03-sso-fields.png" alt="SSO fields" class="img-responsive" />

CoScale supports the HTTP-POST binding for SAML2: urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST
CoScale specifies urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress for the format of the NameIDPolicy in Assertion Requests.

You will have to provide the following in your Identity provider:
* CoScale ACS URL: [https://app.coscale.com/api/v1/sso/acs/](https://app.coscale.com/api/v1/sso/acs/)
* CoScale Entity ID: [https://app.coscale.com/api/v1/sso/metadata/](https://app.coscale.com/api/v1/sso/metadata/)

In return you will get a SSO Url, Entity ID and Certificate, put these into the form. For the certificate, please omit the first and last line containing BEGIN CERTIFICATE and END CERTIFICATE.

For Google SSO specifics see [https://support.google.com/a/answer/6087519?hl=en](https://support.google.com/a/answer/6087519?hl=en)
