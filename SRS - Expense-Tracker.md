
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







