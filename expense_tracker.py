expenses={
    "Food": 200,
    "Transportation": 150,
    "Entertainment": 100
}

total=sum(expenses.values()) 

highest=max(expenses, key=expenses.get)

print("Total expenses:", total  )
print("Highest expense:",highest)
