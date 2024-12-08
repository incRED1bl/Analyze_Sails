from analyze.scripts import *
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go



def draw_correlation():
    exp = expensive_df[info.MONEY].value_counts()
    proportion1_card = (exp['Card'] / exp.sum()) * 100
    proportion1_transaction = (exp['Transaction'] / exp.sum()) * 100
    proportion1_cash = (exp['Cash'] / exp.sum()) * 100

    che = cheap_df[info.MONEY].value_counts()
    proportion2_card = (che['Card'] / che.sum()) * 100
    proportion2_transaction = (che['Transaction'] / che.sum()) * 100
    proportion2_cash = (che['Cash'] / che.sum()) * 100

    labels = ['High-cost', 'Low-cost']
    payment_methods = ['Card', 'Transaction', 'Cash']
    proportions = [[proportion1_card, proportion1_transaction, proportion1_cash], [proportion2_card, proportion2_transaction, proportion2_cash]]

    fig = go.Figure(data=[go.Bar(name=labels[i], x=payment_methods, y=proportions[i], width=0.4) for i in range(len(labels))])
    fig.update_layout(barmode='group', title_text="Proportions", xaxis_title="Payment Method", yaxis_title="Percentage (%)")

    st.plotly_chart(fig)

@st.cache_data()
def draw_pie():
    payment_method_counts = default_df['Payment Method'].value_counts().reset_index()
    payment_method_counts.columns = ['Payment Method', 'Amount']
    average_payment = px.pie(
        payment_method_counts,
        names=info.PAYMENT_METHOD,
        values='Amount',
        title="Payment Methods",
        hole=0.4
    )
    st.plotly_chart(average_payment)


@st.cache_data()
def draw_bar(df):
    cheap_payment_method_counts = df['Collection'].value_counts().reset_index()
    cheap_payment_method_counts.columns = ['Collection', 'Amount']
    cheap_collection_counts = px.bar(
        cheap_payment_method_counts,
        x=info.MONEY,
        y='Amount',
        title="Usage of different methods",
        color=info.MONEY
        )
    st.plotly_chart(cheap_collection_counts)

@st.cache_data()
def count_payment_ranges(df):
    less_500 = df[df[info.TOTAL] < 500].shape[0]
    less_1000 = df[(df[info.TOTAL] >= 500) & (df[info.TOTAL] < 1000)].shape[0]
    less_2000 = df[(df[info.TOTAL] >= 1000) & (df[info.TOTAL] < 2000)].shape[0]
    less_5000 = df[(df[info.TOTAL] >= 2000) & (df[info.TOTAL] < 5000)].shape[0]
    less_10000 = df[(df[info.TOTAL] >= 5000) & (df[info.TOTAL] < 10000)].shape[0]
    less_15000 = df[(df[info.TOTAL] >= 10000) & (df[info.TOTAL] < 15000)].shape[0]
    counts = [less_500, less_1000, less_2000, less_5000, less_10000, less_15000]
    payment_ranges = ['Under 500', '500 to 1000', '1000 to 2000', '2000 to 5000', '5000 to 10000', '10000 to 15000']
    fig = px.pie(names=payment_ranges, values=counts, title="Payment Ranges", hole=0.4)
    st.plotly_chart(fig)

def choose_cheap():
    price_value = st.slider(
        "Choose maximum price for low-cost DataFrame",
        min_value=500,
        max_value=2000,
        value=500,
        step=500)
    print(price_value)
    return Observe.client([['TOTAL', 0, price_value]])


def choose_expensive():
   price_value = st.slider(
       "Choose minimum price for high-cost DataFrame",
       min_value=5000,
       max_value=15000,
       value=5000,
       step=2500
   )
   return Observe.client([['TOTAL', price_value, 20000]])


if __name__ == "__main__":
    default_df = Observe.client([])
    st.header("Project – Analyze of Sales")
    st.divider()
    st.subheader("HYPOTHESIS")
    st.write("If the purchase is expensive, customers are more likely to use alternative payment methods(except cash) such as credit cards, digital wallets, or other electronic payment options.")
    st.divider()
    st.subheader("The Source DataFrame")
    st.dataframe(default_df)
    draw_pie()
    st.write("This pie-chart shows all types of payments that are represented in used dataset.")
    count_payment_ranges(default_df)
    st.write("This graph illustrates the diversified data, so the selection will give objective result in the end of the research.")
    st.divider()
    st.subheader("The low-cost dataframe")
    cheap_df = choose_cheap()
    st.dataframe(cheap_df)
    st.write('Here is a dataframe with selection, that can be narrowed by slider button, presented upwards.')
    st.write('Low-cost means that it makes right-sided limit as a maximum.')
    draw_bar(cheap_df)
    st.write("Visually can be spotted that cash part is approximately equal to a quarter of the total buying operations by different methods.")
    st.write("comment to default selection*")
    st.divider()
    st.subheader("The high-cost dataframe")
    expensive_df = choose_expensive()
    st.dataframe(expensive_df)
    st.write("Here is a dataframe with selection, that can be narrowed by slider button, presented upwards.")
    st.write("High-cost means that it makes left-sided limit as a minimum.")
    draw_bar(expensive_df)
    st.write("Visually can be spotted that cash part is approximately equal to a tenth part of the total buying operations by different methods.")
    st.write("comment to default selection*")
    st.divider()
    st.subheader("The Correlation")
    draw_correlation()
    st.write("To sum up, the correlation is very clear the delta of paying cash for expensive purchases and cheap varies from 5 to 15 percents approximately, it is not very prominent gap, but very stable.")
    st.write("The all selections shows the trend(you can check different configurations) not to pay with cash for expensive purchases, which approves hypothesis.")
    st.write("The fact that the hypothesis was confirmed is not surprising, because people do not want to carry big sums of money, making them easy target and very vulnerable.")
