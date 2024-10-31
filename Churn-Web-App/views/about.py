import streamlit as st

st.markdown(
    """
    <style>
    /* Make the image responsive */
    .responsive-img {
        max-width: 100%;
        height: auto;
    }
    
    /* Adjust column width on smaller screens */
    @media (max-width: 768px) {
        .stColumn > div:first-child {
            width: 100% !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- HERO SECTION WITH IMAGE ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/1.jpg", width=230)

with col2:
    st.title("Understanding and Managing Customer Churn", anchor=False)
    st.write(
        "Customer churn is a critical business metric that refers to the loss of customers over a given period. "
        "Effectively managing churn is essential for maintaining a healthy customer base and ensuring long-term growth."
    )

# --- WHAT IS CHURN? ---
st.write("\n")
st.subheader("What is Churn?", anchor=False)
st.write(
    """
    Customer churn, also known as customer attrition, is the process where customers stop doing business with a company. 
    It's measured as the percentage of customers who leave over a specific time period. 
    Understanding churn helps businesses identify potential issues and areas for improvement.
    """
)

# --- CAUSES OF CHURN ---
st.write("\n")
st.subheader("Causes of Churn", anchor=False)
st.write(
    """
    Churn can result from a variety of factors, including:

    - **Poor Customer Service:** Negative experiences with customer support can lead to dissatisfaction.
    - **Lack of Perceived Value:** When customers feel they're not getting enough value from a product or service, they may seek alternatives.
    - **Competitor Offers:** Better deals or more attractive offerings from competitors can entice customers away.
    - **Product Dissatisfaction:** Issues with product quality, usability, or performance can drive customers to churn.
    """
)

# --- IMPACT OF CHURN ON BUSINESS ---
st.write("\n")
st.subheader("Impact of Churn on Business", anchor=False)
st.write(
    """
    Churn has several negative impacts on a business, including:

    - **Revenue Loss:** Losing customers directly reduces revenue, especially if the cost of acquiring new customers is high.
    - **Reduced Customer Lifetime Value (CLTV):** High churn rates lower the average CLTV, impacting the overall profitability of a company.
    - **Brand Reputation:** A high churn rate can damage a company's reputation, making it harder to attract and retain customers.
    """
)

# --- CHURN PREDICTION AND PREVENTION ---
st.write("\n")
st.subheader("Churn Prediction and Prevention", anchor=False)
st.write(
    """
    To manage churn effectively, businesses can use predictive analytics and targeted strategies:

    - **Predictive Modeling:** By analyzing customer data, businesses can build models to predict which customers are at risk of churning.
    - **Proactive Retention Strategies:** Personalized marketing, improved customer support, loyalty programs, and targeted offers can help retain customers and reduce churn.
    """
)

# --- MEASURING AND MONITORING CHURN ---
st.write("\n")
st.subheader("Measuring and Monitoring Churn")
st.write(
    """
    Regularly measuring and monitoring churn is essential to understanding its impact and taking timely actions:

    - **Churn Rate Calculation:** The churn rate is typically calculated by dividing the number of lost customers by the total number of customers at the start of the period.
    - **Continuous Monitoring:** Keeping an eye on churn metrics helps detect trends and allows businesses to act quickly to mitigate rising churn rates.
    """
)
