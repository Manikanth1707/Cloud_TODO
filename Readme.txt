# Cloud-Based To-Do Application 🚀

This project is a **serverless To-Do application** built using **AWS services**. It enables users to **add, update, delete, and view tasks** while leveraging cloud computing for scalability and performance.

## 🌟 Features
- **User Authentication** with AWS Cognito  
- **Task Management** (Create, Read, Update, Delete)  
- **DynamoDB** for database storage  
- **Serverless Architecture** using AWS Lambda  
- **API Gateway** for RESTful API endpoints  
- **CloudWatch Monitoring** for logs and performance tracking  

## 🛠️ Technologies Used
- **AWS Lambda** – Backend processing  
- **Amazon DynamoDB** – NoSQL database for storing tasks  
- **Amazon API Gateway** – Exposing REST APIs  
- **AWS Cognito** – User authentication  
- **AWS CloudWatch** – Monitoring logs  
- **HTML, CSS, JavaScript** – Frontend development  
- **Git & GitHub** – Version control  

## 📌 Setup & Deployment  
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/cloud-todo-app.git
cd cloud-todo-app
```
### **2️⃣ Install Dependencies**
```sh
npm install
```
### **3️⃣ Deploy to AWS**
- Configure AWS CLI:  
  ```sh
  aws configure
  ```
- Deploy Lambda functions using AWS SAM or manually upload through the AWS Console.

### **4️⃣ Run Locally**
- Open `index.html` in a browser  
- Ensure API Gateway endpoints are correctly configured  

## 📊 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/tasks` | Fetch all tasks |
| POST | `/tasks` | Add a new task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## 💜 License  
This project is open-source and available under the **MIT License**.

---

💡 **Contributions & Issues**  
Feel free to **fork** this repository, submit **pull requests**, or report **issues**!  


