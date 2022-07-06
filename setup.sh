mkdir -p ~/.streamlit/
 
echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
 
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]
primaryColor = '#E694FF'
backgroundColor = '#00172B'
secondaryBackgroundColor = '#0083B8'
textColor = '#FFF'
font = 'sans serif'
" > ~/.streamlit/config.toml
