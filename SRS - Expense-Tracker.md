
# Software Requirements
 This software requirements specification (SRS) comprehensively documents all carefully elicited and analyzed system requirements. By serving as the pivotal foundation for all subsequent development efforts, this SRS seeks to drive effective engineering and delivery of the proposed recipe recommendation system.

## Functional Requirements
### login/signup 

| ID  | Requirement |
| :-------------: | :----------: |
| FR1 | The system SHALL allow users to register an account with their name, email, and a unique username..|
| FR2 | Users SHALL be able to log in securely using their credentials.|
| FR3 | The system SHALL provide options for users to reset their passwords securely.|
| FR4 | Users SHALL have the ability to update their account information.|
| FR5 | The system SHALL validate user credentials during the login process.|


### Input Ingredients

| ID  | Requirement |
| :-------------: | :----------: |
| FR6 | The system SHALL allow users to input a list of ingredients they have or wish to use for cooking.|
| FR7 | The system SHALL validate and process user-inputted ingredients for accurate and relevant recipe recommendations.|
| FR8 | The system SHALL suggest ingredient substitutions based on user choice.|
| FR9 | The system SHALL enable users to edit and modify their ingredient preferences.|
| FR10| The system shall smartly recommend extra ingredients, using user input to improve the variety and completeness of recipes.|

### Recommend Recipes

| ID  | Requirement |
| :-------------: | :----------: |
| FR11 | The system SHALL recommend recipes based on user-inputted ingredients and preferences.|
| FR12 | The system SHALL provide personalized recipe suggestions based on user rating and reviews.|
| FR13 | The system SHALL allow users to filter and sort recipe recommendations based on various criteria. |
| FR14 | The system SHALL continuously update and add new recipes to the recommendation database.|
| FR15 | The system SHALL include a feature that encourages users to explore recipes from different cuisines.|

### view Recipe

| ID | Requirement |
| :-------------: | :----------: |
| FR16 | The system SHALL allow users to search for recipes based on ingredients.|
| FR17 | The system SHALL allow users to view detailed information about a specific recipe.|
| FR18 | The system shall allow the user to save and print the recipe.|
| FR19 | The system SHALL provide an option for users to view the instructions and other details of a recipe.|
| FR20 | The system SHALL display the source or origin of each recipe, providing information about where the recipe was sourced.|

### Save&Print Recipe

| ID | Requirement |
| :-------------: | :----------: |
| FR21 | The system SHALL allow users to save their favorite recipes for quick access.|
| FR22 | The system SHALL provide a printing option for users to print out recipes for offline reference.|
| FR23 | Users SHALL have the capability to create a personalized recipe collection for future use.|
| FR24 | The system SHALL generate print-friendly recipe layouts, ensuring clear and concise printing.|
| FR25 | Users SHALL be able to organize and categorize saved recipes based on personal preferences or occasions.|


### Feedback

| ID  | Requirement |
| :-------------: | :----------: |
| FR26 | The system SHALL allow users to provide feedback on recipes, including comments.|
| FR27 | The system SHALL display average ratings for each recipe based on user feedback.|
| FR28 | The system SHALL enable users to edit or delete their feedback.|
| FR29| The system SHALL store user feedback information for analysis and improvement.|
| FR30 | The system SHALL incorporate a feature allowing users to mark recipes as favorites, providing a convenient way to keep track of preferred dishes for future reference.|

## Non Functional requirements

### Scalability

| ID  | Requirement |
| :-------------: | :----------: |
| NFR31| The system shall support a growing database of recipes and users without significant degradation in performance.|
| NFR32| As the number of concurrent users increases, the system shall maintain consistent response times for recipe searches and recommendations.|
| NFR33| The application shall seamlessly integrate new features and enhancements to accommodate evolving user needs.|
| NFR34|The system shall implement an auto-scaling mechanism to dynamically allocate resources based on the current demand, ensuring optimal performance during peak usage periods.|  
| NFR35||The system shall have a decoupled architecture to enable independent scaling of different components.|

### Performance

| ID  | Requirement |
| :-------------: | :----------: |
| NFR36| The system SHALL respond to multiple users. |
| NFR37| The website SHALL load as fast as possible.|
| NFR38|The system SHALL respond to the user in less than 10 sec.|
| NFR39|The system SHALL provide results for all types of user inputs.|
| NFR40|The system SHALL be feasible to the user.|

### Usability

| ID  | Requirement |
| :-------------: | :----------: |
| NFR41| The user SHALL have a straightforward experience in interacting with recipe recommendations. |
| NFR42| The system SHALL provide a user-friendly design that allows users to access all features easily.|
| NFR43|The user SHALL easily navigate the website's interface to find and explore recipes.|
| NFR44|The system SHALL offer clear and concise guidance to help users make the most of its features. |
| NFR45|The system SHALL facilitate an intuitive and enjoyable user experience without complex navigation.|


### Reliability

| ID  | Requirement |
| :-------------: | :----------: |
| NFR46| The system SHALL remain available for users for at least 99.9% of the time. |
| NFR47| The system SHALL ensure consistent access to recipe recommendations without frequent downtimes. |
| NFR48|The user interface shall facilitate smooth maneuvering.|
| NFR49|The system SHALL provide reliable data consistency during user interactions. |
| NFR50|The data consumption for utilizing recipe recommendations shall be kept at a minimal level for users.|

### Compatibility

| ID  | Requirement |
| :-------------: | :----------: |
| NFR51| The system SHALL run independently with respect to type of machines. |
| NFR52| The System SHALL work effectively with different versions of the software.|
| NFR53| The system SHALL provide ability to share between different machines.|
| NFR54| The system SHALL able to run at different OS environments .|
| NFR55 | The system SHALL able to enhance information exchange with different comnponents of software .|


# Change management plan


## How will you train people to use it?
To ensure a smooth transition and user adoption, a comprehensive training program will be implemented. Initially, an online training session will be conducted for all users, providing step-by-step guidance on navigating the platform, searching for recipes, and utilizing personalized features. Additionally, multi-modal training resources including documentation, videos, live sessions, and in-app chatbots to guide users.

## How will you ensure it integrates within their ecosystem / software?
Our recipe app offers an intuitive interface for easy onboarding. By validating core features like login work, we ensure key requirements are fulfilled. Flexible APIs facilitate data flows between the frontend and backend recommendation systems seamlessly. Cross-platform responsive design allows versatility across devices, thoroughly compatibility tested. Regular feedback refinement improve overall user experience, identifying any outstanding feasibility issues quickly so we can embed this app consistently across existing ecosystems

## How will you ensure that it any discovered issues are resolved?
An efficient issue resolution process will be implemented to address any identified concerns promptly. Users will have access to a dedicated support portal where they can report issues and receive timely updates on the resolution progress. A tiered support system will be established, with a team of technical experts available to tackle complex issues. Regular system audits and automated monitoring tools will be in place to proactively identify and resolve potential issues before users encounter them. Feedback from users will be actively sought and used to drive continuous improvement, ensuring a robust and reliable food recipe recommendation platform.

# Traceability links
This section shows how the requirements are related to other project artifacts, such as class diagrams, use case diagrams, and activity diagrams, as well as how they relate to artifacts, such as class diagrams. 
 

## Use Case Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| UseCase1 | [login / signup](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/UseCase.png.pdf)| FR1-FR5 |
| UseCase2 | [Input Ingredients]( https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/UseCase.png.pdf)| FR6-FR10 |
| UseCase3 | [Recommend recipes](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/UseCase.png.pdf)| FR11-FR15 |
| UseCase4 | [View Recipe](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/UseCase.png.pdf )| FR16-FR20 |
| UseCase5 | [Save Recipe](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/UseCase.png.pdf)| FR21-FR25 |
| UseCase5 | [Print Recipe](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/UseCase.png.pdf)| FR21-FR25 |
| UseCase6 | [Leave Comments](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/UseCase.png.pdf)| FR26-FR30 |


## Activity Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| 1 | [login/signup/User Information](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Activity%20Diagram.drawio.png)| FR1-FR5, NFR36, NFR38, NFR39, NFR45, NFR46 , NFR48 |
| 2 | [Give Ingredients]( https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Activity%20Diagram.drawio.png)| FR6-FR10, NFR48, NFR49 |
| 3 | [Recommend Recipes]( https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Activity%20Diagram.drawio.png )| FR11,FR12,FR14,FR15,NFR31,NFR33,NFR41,NFR47,NFR50 |
| 4 | [View Recipes]( https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Activity%20Diagram.drawio.png )| FR16-19 NFR41, NFR43, NFR44,NFR45 |
| 5 | [Filter Recipes](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Activity%20Diagram.drawio.png )| TBD |
| 6 | [Save & Print Recipes](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Activity%20Diagram.drawio.png) | FR18, FR21-25,NFR43,NFR44,NFR45 |
| 7 | [Feedback](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Activity%20Diagram.drawio.png)| FR26-30,NFR33,NFR37,NFR38,NFR45,NFR46,NFR47 |


## Class Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| 1 | [login / signup/User](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/class%20diagram-drawio.png)| FR1-5, NFR36, NFR38, NFR39, NFR45, NFR46 , NFR48|
| 2 | [Preferred ingredients](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/class%20diagram-drawio.png)|FR6-FR10, NFR48, NFR49 |
| 3 | [Filtering engine](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/class%20diagram-drawio.png)| FR13,NFR36, NFR37 |
| 4 | [Recipe Recommendation](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/class%20diagram-drawio.png)| FR11,FR12,FR14,FR15,NFR31,NFR32,NFR41,NFR47,NFR50 |
| 5 | [View recipe](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/class%20diagram-drawio.png)| FR16-19, NFR36, NFR38, NFR39,NF42 |
| 6 | [Feedback](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/class%20diagram-drawio.png)| FR26-30, NFR28,NFR32,NFR33,NFR40,NFR41,NFR42 |

## Object Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| 1 | [login / signup/User](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/object%20diagram.jpg)| FR1-5, NFR36, NFR38, NFR39, NFR45, NFR46 , NFR48 |
| 2 | [Preferred ingredients](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/object%20diagram.jpg)| FR6-FR10, NFR48, NFR49 |
| 3 | [Filtering engine]( https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/object%20diagram.jpg)| FR13,NFR36, NFR37 |
| 4 | [Recipe Recommendation](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/object%20diagram.jpg)| FR11,FR12,FR14,FR15,NFR31,NFR32,NFR41,NFR47,NFR50 |
| 5 | [View recipe](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/object%20diagram.jpg)| FR16-19, NFR36, NFR38, NFR39,NF42 |
| 6 | [Feedback](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/object%20diagram.jpg)| FR26-30, NFR28,NFR32,NFR33,NFR40,NFR41,NFR42 |


## WIndows Navigation Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| 1 | [Create Account Form](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Navdiagram.png ) | FR1-5, NFR31, NFR33, NFR34, NFR40, NFR41 , NFR43 |
| 2 | [Select Ingredient Form](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Navdiagram.png) | FR6-FR10, NFR43, NFR44 |
| 3 | [Recipes List]( https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Navdiagram.png) | FR11, FR12, FR14, FR15,NFR26, NFR27, NFR36, NFR42, NFR45|

# Software Artifacts
Here we can find all related use case, activity, window navigation, class diagrams and Object diagram of our food recipe recommendation project

* [ Use case diagram ](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/UseCase.png.pdf)
* [ Activity diagram ]( https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Activity%20Diagram.drawio.png)
* [ Class diagram ](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/class%20diagram-drawio.png)
* [ Object diagram ](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/object%20diagram.jpg)
* [ Window navigations diagrams ](https://github.com/shankymurali/GVSU-CIS-641-4WIZ/blob/main/artifacts/Navdiagram.png)





