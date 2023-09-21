# Fast Food Menu Application 🍔

This is our final project, which we successfully completed during our time at Per Scholas. Throughout this journey, my team and I emphasized the significance of following established Software Development Life Cycle (SDLC) principles and embracing Agile development methodologies for effective collaboration.
<br><br>
<img width="1183" alt="Screenshot 2023-09-21 at 4 38 24 PM" src="https://github.com/niazkhan0731/Fastfood-Menu-Project/assets/135728087/1a87ca0d-198c-4d5f-a05c-608c34d0bf85">
<br><br>
In a real-world, collaborative environment, we embarked on the creation of a Fast Food Menu Application. Leveraging a diverse set of technologies, including HTML, CSS, Python, Flask, and AWS Services such as EC2, Cloud9, and MariaDB, we aimed to demonstrate the power of a well-structured development process.

By adhering to SDLC, we ensured that our project was well-organized, with clearly defined stages, requirements, and goals. This systematic approach allowed us to efficiently manage our project's scope, track progress, and address issues as they arose.

Additionally, our adoption of Agile methodologies fostered collaboration among team members, promoting flexibility and adaptability throughout the development process. Agile practices, such as regular stand-up meetings and iterative development, enabled us to respond to changing requirements and feedback from stakeholders promptly.

As a result of our commitment to SDLC and Agile methodologies, we were able to bring this Fast Food Menu Application to life successfully. Below, I'll provide an overview of the steps we took to make it all happen and where you can experience the project in action.

## Step 1: Github Collaboration

Our journey began with a strategic act: establishing the project's heartbeat on GitHub. I initiated the repository and promptly invited my team members as collaborators. This foundational step ensured that we could work seamlessly together, employing version control to keep our project on the path to success.

## Step 2: Starting with index.html

With our collaboration environment solidified, we delved into crafting the very essence of our application—the user interface. Our HTML masterpiece, known as index.html, laid the groundwork for the front-end. To maintain best practices, we placed this file within the 'templates' folder—a choice that holds is vital for our Flask-based application. It is here that Flask would later draw the templates required for rendering dynamic content.

## Step 4: Styling with styles.css

As the saying goes, "First impressions matter". We were determined to ensure that our application not only functioned flawlessly but also radiated aesthetic appeal. The styles.css file underwent meticulous curation to elevate the user experience and present an engaging, unified design. To maintain best practices, we housed this style file within the 'static' folder. This strategic placement was essential to facilitate Flask's streamlined access to the styles, ensuring that our application looked polished and consistent across all its web pages.

## Step 5: Making app.py work

Our project came to life with the development of app.py. This Python script was the engine powering our Fast Food Menu Application, connecting the front-end and back-end seamlessly. We carefully coded it to ensure that data flowed from index.html to receipt.html, allowing users to interact with the application as intended.

# Step 6: Connecting databaselogic.py

We made the decision to connect to and store all real-time data in a MySQL database. To achieve this, we utilized databaselogic.py to develop the necessary code for our application. This code enables our application not only to establish connections and display a list of available items for sale but also to seamlessly transmit calculations performed in the background by app.py directly to our database in real-time. As a practical example, this approach allows our company to continually monitor key details such as the date an order was placed, the specific item ordered, its quantity, and the total order amount.

## Step 6: Leveraging AWS Services - Cloud9

To host and manage our application, we harnessed the capabilities of AWS Services, particularly Cloud9. This cloud-based integrated development environment offered the scalability and accessibility we needed to effectively develop, test, and deploy our project. The cloud environment made collaboration even smoother, enabling us to work on the project from anywhere.

## Step 7: Harnessing AWS Services - MariaDB

Our project's data management relied on the robust MariaDB, an integral component of our AWS infrastructure. This relational database ensured data integrity, security, and efficiency. It played a crucial role in storing and retrieving the information needed to deliver a seamless user experience.

# Challenges

Our journey was not without its challenges. Debugging app.py to ensure the seamless transfer of data between index.html and receipt.html, especially after intricate mathematical operations, posed a significant hurdle. Additionally, configuring the EC2 instance's security group to allow public access and enabling SSH ports for remote CLI access required careful consideration and attention to security best practices.

# Conclusion

The culmination of our hard work and dedication is showcased in this repository, housing all the files and code for our Fast Food Menu Application. Throughout this project, we embraced the best practices of Software Development Life Cycle (SDLC), delivering a solution that demonstrates our commitment to excellence in software engineering.

As I embark on my journey towards a bachelor's degree in computer science and continue to expand my knowledge in the field, I eagerly anticipate the opportunity to apply my skills and collaborate on innovative projects like this one.

In conclusion, our project represents not just an endpoint but the dawn of a new chapter. Beyond this cohort, our team stands ready and enthusiastic to sustain our collaboration, evolving this project into a fully operational, dynamic website enriched with an array of functions. The realm of possibilities is boundless, and we are exhilarated by the prospect of breathing life into our myriad ideas, armed with the knowledge and tools to transform them into reality. Together, we remain steadfast in our commitment to applying agile methodologies, ensuring that this project continues to flourish and serve as a beacon of innovation.
