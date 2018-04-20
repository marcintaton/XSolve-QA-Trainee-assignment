# XSolve QA Trainee recruitment task

<br>

## Testing cases for provided registration form

<br>

### Pre-conditions
Based on assumptions made regarding specific input fields 
 * **First name**: must be filled with string of characters. No digits or special signs allowed. Fullstop (.) and hyphen (-) are allowed.
 * **Last name**: must be filled with string of characters. No digits or special signs allowed. Fullstop (.), apostrophe (`) and hyphen (-) are allowed.
 * **Company**: must be filled with string of characters.
 * **E-mail**: if filled, must contain a valid email adress consisting of name, @ and domain name with a dot separator ie: name@domain.com .
 * **I would like to attend the after-party** cheeckbox: if checked, must reveal two remaining fields.
 * **Food preferences** dropdown list: no requirements since there is a default option. "No special preferences" is the default option.
 * **Phone number**: must be filled with string of digits. A single plus (+) at the beginning is allowed. Spaces are allowed but will be trimmed after submission.

### Post conditions
* The form is successfully submited

### Other assumptions
* Whenever form submition fails, the registration forms notifies user which field(s) failed the pre-conditions check (example below). This will allow us to apply changes between test cases to multiple fields, allowing to reduce test cases' count, while retaining test accuracy. Should such feature be unavailable a tast case would have to be made for every possible input combination.

![alt text](/example.png)

## Test cases

In order to fully test the registration form at least two test cases must be made for every required field in the registration form. This task has to be performed twice: with checkbox checked and unchecked.

### These are test cases for unchecked checkbox, testing different name, surname and email variations:

### Case 1.1
Input:
* **First name**: Name
* **Last name**: Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: false

Expected output:
* Success

### Case 1.2
Input:
* **First name**: Name Jr.
* **Last name**: Surname Jr.
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: false

Expected output:
* Success

### Case 1.3
Input:
* **First name**: Name-SecondName
* **Last name**: Surname-SecondSurname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: false

Expected output:
* Success

### Case 1.4
Input:
* **First name**: Name-SecondName Jr.
* **Last name**: Surname-SecondSurname Jr.
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: false

Expected output:
* Success

### Case 1.5
Input:
* **First name**: Name
* **Last name**: O`Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: false

Expected output:
* Success

### Case 1.6
Input:
* **First name**: Name0
* **Last name**: Surname123
* **Company**: CompanyName
* **Email**: namedomaincom
* **Checkbox**: false

Expected output:
* Failure due to **First name** containg digit
* Failure due to **Last name** containg digit
* Failure due to **Email** having invalid format

### Case 1.7
Input:
* **First name**: Name*
* **Last name**: #Surname
* **Company**: CompanyName
* **Email**: name@domaincom
* **Checkbox**: false

Expected output:
* Failure due to **First name** containg forbidden special characters
* Failure due to **Last name** containg forbidden special characters
* Failure due to **Email** having invalid format

### Case 1.8
Input:
* **First name**: N`ame
* **Last name**: Sur-na-me
* **Company**: CompanyName
* **Email**: namedomain.com
* **Checkbox**: false

Expected output:
* Failure due to **First name** containg forbidden special characters
* Failure due to **Email** having invalid format

### These are test cases for checked checkbox, testing different name, surname and email variations, while **Food preferences** and **Phone number** remain valid:


### Case 2.1
Input:
* **First name**: Name
* **Last name**: Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: 123456789

Expected output:
* Success

### Case 2.2
Input:
* **First name**: Name Jr.
* **Last name**: Surname Jr.
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: 123456789

Expected output:
* Success

### Case 2.3
Input:
* **First name**: Name-SecondName
* **Last name**: Surname-SecondSurname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: 123456789

Expected output:
* Success

### Case 2.4
Input:
* **First name**: Name-SecondName Jr.
* **Last name**: Surname-SecondSurname Jr.
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: 123456789

Expected output:
* Success

### Case 2.5
Input:
* **First name**: Name
* **Last name**: O`Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: 123456789

Expected output:
* Success

### Case 2.6
Input:
* **First name**: Name0
* **Last name**: Surname123
* **Company**: CompanyName
* **Email**: namedomaincom
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: 123456789

Expected output:
* Failure due to **First name** containg digit
* Failure due to **Last name** containg digit
* Failure due to **Email** having invalid format

### Case 2.7
Input:
* **First name**: Name*
* **Last name**: #Surname
* **Company**: CompanyName
* **Email**: name@domaincom
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: 123456789

Expected output:
* Failure due to **First name** containg forbidden special characters
* Failure due to **Last name** containg forbidden special characters
* Failure due to **Email** having invalid format

### Case 2.8
Input:
* **First name**: N`ame
* **Last name**: Sur-na-me
* **Company**: CompanyName
* **Email**: namedomain.com
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: 123456789

Expected output:
* Failure due to **First name** containg forbidden special characters
* Failure due to **Email** having invalid format

### These are test cases for checked checkbox, testing different Food preferences and Phone number variations, while all other fields remain valid:

### Case 2.9
Input:
* **First name**: Name
* **Last name**: Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: Vegan
* **Phone number**: 123456789

Expected output:
* Success

### Case 2.10
Input:
* **First name**: Name
* **Last name**: Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: Vegetarian
* **Phone number**: 123456789

Expected output:
* Success

### Case 2.11
Input:
* **First name**: Name
* **Last name**: Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: Food allergies
* **Phone number**: 123456789

Expected output:
* Success

### Case 2.12
Input:
* **First name**: Name
* **Last name**: Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: +123456789

Expected output:
* Success

### Case 2.13
Input:
* **First name**: Name
* **Last name**: Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: 12345+6789

Expected output:
* Failure due to **Phone number** having **+** sign at forbidden position

### Case 2.14
Input:
* **First name**: Name
* **Last name**: Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: +123456=789ah

Expected output:
* Failure due to **Phone number** containig other characters than digits, spaces and plus

### Case 2.15
Input:
* **First name**: Name
* **Last name**: Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: +1234 56789

Expected output:
* Success

### Case 2.16
Input:
* **First name**: Name
* **Last name**: Surname
* **Company**: CompanyName
* **Email**: name@domain.com
* **Checkbox**: true
* **Food preferences**: No special preferences
* **Phone number**: 1234 56789

Expected output:
* Success