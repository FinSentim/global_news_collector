# global_news_collector

The goal of this project is to collect articles from supproted websites

## Setup

### Install dependencies

run 'pip install -r requirements.txt'

## How to contribute

- Clone the repository
- Run the setup script
- Run the tests (`python -m unittest`)
- Select the Github issue you want to work on
- Create a branch from main branch, name appropriately (e.g. `123-fix-something` where 123 is the issue number and `fix-something` is the issue title)
- Implement/fix the feature
- Ensure that the code works, run the tests (`python -m unittest`)
- Rebase on master (fix any conflicts)
- Open a pull request
- Make sure CircleCI tests pass

## Supported websites

To be updated

## For each supported websites functions


function **get_article(url)** that accepts a link to an article and returns a dictionary with the following keys:
    date_published: date of publication
    date_retrieved: date of retrieval
    url: url of the article
    title: title of the article
    publisher: Company or website that published the article
    publisher_url: url of the publisher
    author: author of the article
    body: text of the article
    
