Below is the **complete raw `README.md` code**.  
You can **copy–paste this directly** into a `README.md` file.  
✅ No content skipped  
✅ No formatting mistakes  
✅ Proper Markdown syntax throughout

***

````md
# MongoDB CRUD Operations using Student Schema

## Aim
Perform MongoDB CRUD operations:
- Insert
- Insert Many
- Find
- Update
- Update Many
- Delete
- Delete Many

---

## Software Requirements

- MongoDB Community Server
- Mongo Shell (mongosh)

Download MongoDB:

https://www.mongodb.com/try/download/community

---

## Start MongoDB Server

Open terminal:

```bash
mongod
````

Open another terminal:

```bash
mongosh
```

***

## Create Database

```javascript
use collegeDB
```

***

## Student Collection Schema

```javascript
{
    name: String,
    rollNo: Number,
    department: String,
    year: Number,
    age: Number,
    marks: Number,
    city: String
}
```

***

## Insert One Document

```javascript
db.students.insertOne({
    name: "Mangesh Pawar",
    rollNo: 101,
    department: "AI&DS",
    year: 4,
    age: 22,
    marks: 91,
    city: "Pune"
})
```

***

## Insert Multiple Documents

```javascript
db.students.insertMany([
    {
        name: "Rahul Sharma",
        rollNo: 102,
        department: "AI&DS",
        year: 4,
        age: 21,
        marks: 85,
        city: "Mumbai"
    },
    {
        name: "Sneha Patil",
        rollNo: 103,
        department: "Computer",
        year: 3,
        age: 20,
        marks: 78,
        city: "Nashik"
    },
    {
        name: "Amit Joshi",
        rollNo: 104,
        department: "IT",
        year: 2,
        age: 19,
        marks: 67,
        city: "Pune"
    },
    {
        name: "Priya Deshmukh",
        rollNo: 105,
        department: "AI&DS",
        year: 4,
        age: 22,
        marks: 95,
        city: "Nagpur"
    }
])
```

***

## Show All Documents

```javascript
db.students.find()
```

***

## Find One Document

```javascript
db.students.findOne({ name: "Rahul Sharma" })
```

***

## Find Specific Fields

```javascript
db.students.find(
    {},
    { name: 1, marks: 1, _id: 0 }
)
```

***

## Find Students with Marks Greater Than 80

```javascript
db.students.find({ marks: { $gt: 80 } })
```

***

## Find Students from Pune

```javascript
db.students.find({ city: "Pune" })
```

***

## Find Students from AI\&DS Department

```javascript
db.students.find({ department: "AI&DS" })
```

***

## Update One Document

```javascript
db.students.updateOne(
    { rollNo: 102 },
    { $set: { marks: 90 } }
)
```

***

## Update Multiple Documents

```javascript
db.students.updateMany(
    { department: "AI&DS" },
    { $set: { year: 5 } }
)
```

***

## Increment Marks

```javascript
db.students.updateOne(
    { rollNo: 103 },
    { $inc: { marks: 5 } }
)
```

***

## Rename Field

```javascript
db.students.updateMany(
    {},
    { $rename: { "department": "dept" } }
)
```

***

## Add New Field

```javascript
db.students.updateMany(
    {},
    { $set: { college: "DY Patil Institute" } }
)
```

***

## Delete One Document

```javascript
db.students.deleteOne({ rollNo: 104 })
```

***

## Delete Multiple Documents

```javascript
db.students.deleteMany({ city: "Pune" })
```

***

## Delete All Documents

```javascript
db.students.deleteMany({})
```

***

## Drop Collection

```javascript
db.students.drop()
```

***

## Show Databases

```javascript
show dbs
```

***

## Show Collections

```javascript
show collections
```

***

## Sort Students by Marks

```javascript
db.students.find().sort({ marks: -1 })
```

***

## Limit Records

```javascript
db.students.find().limit(2)
```

***

## Count Documents

```javascript
db.students.countDocuments()
```

***

## MongoDB Operators

| Operator | Meaning            |
| -------- | ------------------ |
| $gt      | Greater Than       |
| $lt      | Less Than          |
| $gte     | Greater Than Equal |
| $lte     | Less Than Equal    |
| $set     | Set Value          |
| $inc     | Increment Value    |
| $rename  | Rename Field       |

***

## Example Output

```javascript
{
    name: 'Mangesh Pawar',
    rollNo: 101,
    department: 'AI&DS',
    year: 4,
    age: 22,
    marks: 91,
    city: 'Pune'
}
```

***

## Viva Questions

### 1. What is MongoDB?

MongoDB is a NoSQL document-oriented database.

***

### 2. What is CRUD?

CRUD stands for:

*   Create
*   Read
*   Update
*   Delete

***

### 3. What is a Collection?

A collection is a group of MongoDB documents.

***

### 4. Difference between SQL and MongoDB?

| SQL    | MongoDB    |
| ------ | ---------- |
| Table  | Collection |
| Row    | Document   |
| Column | Field      |

***

### 5. What is insertMany()?

It inserts multiple documents into a collection.

***

### 6. What is updateMany()?

It updates multiple matching documents.

***

### 7. What is deleteMany()?

It deletes multiple matching documents.

***

## Conclusion

Successfully performed MongoDB CRUD operations:

*   Insert
*   Query
*   Update
*   Delete

using Student collection schema.

```

---

If you want, I can also:
- ✅ Add **screenshots section**
- ✅ Convert it into **college practical format**
- ✅ Optimize it for **GitHub portfolio**
- ✅ Add **index, author, and date**

Just tell me 👍
```
