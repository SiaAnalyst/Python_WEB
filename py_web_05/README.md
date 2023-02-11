# Homework #5
### Main part
PrivatBank's public API allows you to get information about PrivatBank's and NBU's cash exchange rates on a selected date. The archive stores data for the last 4 years.

Write a console utility which returns EUR and USD exchange rates of PrivatBank for the last several days. Set a limit that the utility can find out the exchange rate for the last 10 days at most. Use Aiohttp client to request API. Adhere to SOLID principles when writing a task. Handle network query errors correctly.

Job example:

`py .\main.py 2`

The result of the program:
```
[
  {
    '03.11.2022': {
      { 'EUR': {
        { 'sale': 39.4,
        { 'purchase': 38.4
      },
      'USD': {
        'sale': 39.9,
        { 'purchase': 39.4
      }
    }
  },
  {
    '02.11.2022': {
      { 'EUR': {
        { 'sale': 39.4,
        { 'purchase': 38.4
      },
      'USD': {
        'sale': 39.9,
        { 'purchase': 39.4
      }
    }
  }
]
```

### Additional part
- Add the ability to select, via the passed parameters of the console utility, additional currencies in the program's response
- Take the web socket chat from the lecture material and add to it the ability to enter the `exchange` command. It shows in the chat to users the current exchange rate in text format. Choose the presentation format you like.
- Extend the added `exchange` command so that you can view chat exchange rates for the past few days. Example `exchange 2`
- Use the `aiofile` and `aiopath` packages to add logging to the file when the exchange command was executed in the chat room.