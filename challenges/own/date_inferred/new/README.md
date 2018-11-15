# Primitive date format inferrer
Given 
- a listing of date strings in uknown date format and 
- an enum class which contains allowed/supported date formats,  

complete the `get_dates` method.

Although the following assignment text is wordy, once you will see test cases the task definition will become clearer.

The `get_dates` method will return a list of date strings in the format yyyy-mm-dd. The date format of input date strings will be inferred based on the most prevalent allowed date format of items in the list. Allowed/supported date formats are defined in an enum class.

The most prevalent allowed date format of items must represent a single most frequent date format. If there are two most frequent formats with the same frequency raise a custom exception `InfDateFmtError`.

Items in an input list can be in any format no matter whether or not this format is listed in an enum class. Items can be even values which cannot represent a date at all. Those items are nonparsable. If the frequency of nonparsable elements is higher then the frequency of other allowed date formats (counted individually for each format) raise a custom exception `InfDateFmtError`.

Once you have the most prevalent date format, parse dates in an input list and return them as a list of strings in the format yyyy-mm-dd. Dates which are not parsable replace with the string "Invalid".

Important note: the list of allowed/supported date formats is supposed to be stored in an enum class only. The list allowed/supported date formats can be amended when a different enum is passed as an argument (DF). 


As a hint, you are provided with a helper method `_maybe_DFs` which shows how to work with an enum class.

---
This assignment introduces a very simple date format inferrer.
For more serious work you can check:
- dateparser https://dateparser.readthedocs.io
- dateinfer https://github.com/jeffreystarr/dateinfer
