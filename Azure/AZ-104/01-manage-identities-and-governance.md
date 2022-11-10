#### Topics
- Managing Azure active directory
- Subscription and governance

#### Azure Active Directory
- Cloud based identity and directory management service enablinb access to Azure services and other SaaS solutions like Microsoft 365, DropBox, Concur, Salesforce etc.
- Offers self-service options including: 
  - password reset
  - authentication
  - device management
  - hybrid identities
  - single sign-on
- https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis

#### Concepts
  - **Identity**
    - Any object that can be authenticated is considered as an identity. It could be a:
      - user
      - group
      - managed identity ==> identities of Azure resources
      - service principals ==> similar to service accounts on on-premise environments.
  - **Account**
    - When we associate data attributes to an identity, we call it an account. For example, a user will have multiple attributes like location, department, manager, phone number etc. 
  - **Azure AD account**
    - Accounts that are created in Azure AD or another Microsoft cloud service is known as Azure AD Account. 
  - **Azure AD tenant or directory**
    - Dedicated isntance of Azure AD that is created during the sign-up of any Microsoft cloud service subscription. Tenant and directory means the same and you can use interchangeably. 


#### Azure AD join
#### Self-Service Password Reset (SSPR)
#### User Accounts
#### Group Accounts
#### Multi-tenant environments