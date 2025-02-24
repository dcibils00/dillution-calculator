import streamlit as st

st.title("Equity and Dilution Calculator")

# Input fields
pre_money_valuation = st.number_input("Pre-money Valuation", min_value=0.0, value=5000000.0)
investment_amount = st.number_input("Investment Amount", min_value=0.0, value=3000000.0)
post_money_valuation = st.number_input("Post-money Valuation", min_value=0.0, value=15000000.0)

num_founders = st.number_input("Number of Founders", min_value=1, value=4, step=1)

founders = []
for i in range(num_founders):
    col1, col2 = st.columns(2)  # Use columns for better layout
    with col1:
        founder_name = st.text_input(f"Founder {i+1} Name", f"Founder {i+1}")
    with col2:
        founder_ownership = st.number_input(f"Founder {i+1} Ownership (%)", min_value=0.0, value=25.0, max_value=100.0)
    founders.append({"name": founder_name, "ownership": founder_ownership / 100})  # Store as decimals



if st.button("Calculate"):
    if post_money_valuation <= pre_money_valuation + investment_amount:
        st.error("Post-money valuation must be greater than pre-money + investment. Check your inputs.")

    else:
        # Calculations
        investor_ownership = investment_amount / post_money_valuation
        original_owners_ownership = 1 - investor_ownership

        st.subheader("Results")

        st.write(f"Investor Ownership: {investor_ownership * 100:.2f}%")

        st.write("Founder Ownership:")
        for founder in founders:
            new_ownership = founder["ownership"] * original_owners_ownership
            st.write(f"- {founder['name']}: {new_ownership * 100:.2f}%")

        st.write(f"Pre-money Valuation: ${pre_money_valuation:,.2f}")
        st.write(f"Investment Amount: ${investment_amount:,.2f}")
        st.write(f"Post-money Valuation: ${post_money_valuation:,.2f}")


        # Dilution details
        st.subheader("Dilution Details")
        st.write("How much did each founder get diluted:")
        for founder in founders:
            dilution = founder["ownership"] - (founder["ownership"] * original_owners_ownership)
            st.write(f"- {founder['name']}: {dilution*100:.2f}%")

        # Cap table display (optional, but very useful)
        st.subheader("Cap Table")
        cap_table_data = []
        for founder in founders:
            new_ownership = founder["ownership"] * original_owners_ownership
            cap_table_data.append({"Stakeholder": founder['name'], "Pre-Investment": f"{founder['ownership']*100:.2f}%", "Post-Investment": f"{new_ownership*100:.2f}%"})
        cap_table_data.append({"Stakeholder": "Investors", "Pre-Investment": "0.00%", "Post-Investment": f"{investor_ownership*100:.2f}%"})

        st.dataframe(cap_table_data)