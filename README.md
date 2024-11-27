

Sales Data Normalization and Visualization Project 📊💻

Overview
This project demonstrates how to clean, normalize, and visualize customer sales data. The process includes SQL normalization for efficient data storage and management, followed by interactive visualizations created using **Python** (with **Matplotlib** and **Seaborn**) and **Tableau**. This workflow ensures both performance optimization and insightful decision-making.

Tech Stack
- **SQL** (SQLite) for database creation and normalization
- **Python** for data manipulation and visualization (Pandas, Matplotlib, Seaborn)
- **Tableau** for advanced, interactive data visualization (via CSV export or direct SQL connection)

Features
- **SQL Normalization**: Transform raw sales data into structured, optimized tables for easier analysis.
- **Data Extraction**: Query and aggregate sales data to identify trends and insights.
- **Visualizations**: Create bar charts, pie charts, and heatmaps to uncover key sales trends.
- **Exportable Data**: Export the normalized dataset for visualization in Tableau.
  
Steps to Run

1. Clone the Repository 
   Download or clone the repository to your local system.

2. **Install Required Libraries**  
   Install the necessary libraries for Python and SQL.

   ```bash
   pip install sqlalchemy sqlite3 pandas matplotlib seaborn
   ```

3. Run the Jupyter Notebook  
   Open the Jupyter Notebook (`sales_data_analysis.ipynb`), which contains all the code for:
   - SQL database creation and normalization
   - Data extraction using SQL queries
   - Data visualization using **Matplotlib** and **Seaborn**

   To run the notebook, open a terminal and start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

4. Export Data for Tableau  
   Once the visualizations are ready in Python, export the processed data to a **CSV file** for Tableau visualization.
   ```python
   df.to_csv('sales_data_for_tableau.csv', index=False)
   ```

5. **Upload to Tableau**  
   You can now upload the `sales_data_for_tableau.csv` to Tableau Public or Tableau Server to create an interactive dashboard, or connect Tableau directly to the SQL database for real-time visualization.

---

Project Walkthrough

1. **Step 1: Database Creation & Normalization**
   - The **Customers**, **Products**, and **Purchases** tables are created in SQLite.
   - Data is normalized to eliminate redundancy and ensure data integrity.

2. **Step 2: Data Extraction and Analysis**
   - SQL queries aggregate the normalized data to uncover key insights, like total spend by customer and product.

3. **Step 3: Data Visualization**
   - The results are visualized in Python using **Matplotlib** and **Seaborn** for insightful, easily interpretable graphics.

4. **Step 4: Tableau Visualization**
   - The processed data is exported as a **CSV** and can be uploaded to **Tableau** for advanced visual exploration and interactive dashboards.

---

Example Visualizations
- **Bar Chart**: Total spend by customer, categorized by product.
- **Pie Chart**: Share of total spend by product category.
- **Scatter Plot**: Customer segmentation based on purchase frequency and spend.
- **Heatmap**: Sales distribution by region or time of day.

Deployment
- **SQL Database**: Local SQLite database used for normalization.
- **Python**: Jupyter Notebook for running the normalization and analysis code.
- **Tableau**: Create interactive dashboards and visualizations from the exported CSV or SQL connection.



Additional Notes
- The project showcases how to efficiently handle large datasets with normalization and extract meaningful insights.
- For a more advanced setup, you can use cloud databases (e.g., PostgreSQL, MySQL) instead of SQLite for a production-level application.
- Tableau allows for **real-time dashboard deployment** if connected to your SQL database.

License
This project is licensed under the MIT License.

