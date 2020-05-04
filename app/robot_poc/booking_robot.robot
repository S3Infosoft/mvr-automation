*** Settings ***
Library           SeleniumLibrary
Library           String
Library           Collections
Library           unicodedata

*** Variables ***
${url}            http://booking.com
@{abc}            12
&{abcd}           user=sanskar    password=sanskar
${driver}         ${EMPTY}
${agent}          booking
${checkin}        26/05/2020
${checkout}       12/06/2020
${hotel_id}       4216443
${hotel_name}     Mango Valley Resort Ganpatipule
${search_text}    Ratnagiri
${month_diff}     0
@{room_typeids}    room_type_id_421644306    room_type_id_421644302    room_type_id_421644305    room_type_id_421644303
@{room_priceids}    421644306_174652031_0_42_0    421644302_141698786_0_42_0    421644302_174652031_0_42_0    421644305_174652031_0_42_0    421644303_174652031_0_42_0
&{result_data}

*** Test Cases ***
test1
    [Setup]    Log To Console    Test started
    Open Browser    https://robotframework.org/#libraries    chrome
    Close Browser
    Log To Console    Completed suucessfully

test2
    [Tags]    test2
    Open Browser    ${url}    chrome

test3
    Open Browser    ${url}    chrome
    Login
    Close All Browsers

test4
    main_run    ${agent}    ${hotel_id}    ${search_text}    ${checkin}    ${checkout}    ${hotel_name}

*** Keywords ***
login
    [Documentation]    just a dummy to show how keywords work
    Input Text    id=txtUsername    Admin
    Input Password    id=txtPassword    admin
    Click Button    id=btnLogin

start_driver
    ${list} =    Create List    --headless    --disable-gpu    --no-sandbox    --disable-dev-shm-usage    enable-automation    --disable-extensions    --dns-prefetch-disable
    ${args} =    Create Dictionary    args=${list}
    Open Browser

main_run
    [Arguments]    ${agent}    ${hotel_prop}    ${search_text}    ${din}    ${dout}    ${hotel_name}
    ${time1} =    Evaluate    '{dt.day}-{dt.month}-{dt.year}'.format(dt=datetime.datetime.now())    modules=datetime
    ${time1} =    Convert To String    ${time1}
    Open Browser    https://www.booking.com/    chrome
    Maximize Browser Window
    @{checkin_date} =    Split String    ${din}    /
    Log To Console    @{checkin_date}
    ${cin} =    Get From List    ${checkin_date}    0
    ${month} =    Get From List    ${checkin_date}    1
    ${year} =    Get From List    ${checkin_date}    2
    @{checkout_date} =    Split String    ${dout}    /
    ${cout} =    Get From List    ${checkout_date}    0
    ${month_out} =    Get From List    ${checkout_date}    1
    ${year_out} =    Get From List    ${checkout_date}    2
    ${datein} =    Catenate    ${year}    -    ${month}    -    ${cin}
    ${dateout} =    Catenate    ${year_out}    -    ${month_out}    -    ${cout}
    ${datein}=    evaluate    '${datein}'.replace(' ','')
    ${dateout}=    evaluate    '${dateout}'.replace(' ','')
    Log To Console    ${datein}
    Log To Console    ${dateout}
    @{weeks} =    calender_ctrl_new    ${agent}    ${cin}    ${cout}    ${din}    ${dout}    ${datein}    ${dateout}
    Log To Console    ${weeks}
    Input Text    //*[@id="ss"]    ${search_text}
    Click Button    //*[@id="frm"]/div[1]/div[4]/div[2]/button
    Sleep    1s
    ${listed}=    listing    ${hotel_prop}
    Log To Console    ${listed}
    hotel_find    ${hotel_prop}
    Switch Window    NEW
    Log To Console    ab
    Sleep    5s
    Press Keys    None    ESC
    ${data}=    data_scraping
    Set To Dictionary    ${result_data}    start_time    ${time1}
    Set To Dictionary    ${result_data}    end_time    ${time1}
    Set To Dictionary    ${result_data}    ota    ${agent}
    Set To Dictionary    ${result_data}    check_in    ${din}
    Set To Dictionary    ${result_data}    check_out    ${dout}
    Set To Dictionary    ${result_data}    listed_position    ${listed}
    ${d}=    Create Dictionary
    ${len}=    Get Length    ${data}
    Set To Dictionary    ${result_data}    rates    ${data}
    Set To Dictionary    ${result_data}    Status    OK
    Set To Dictionary    ${result_data}    hotel_name    ${hotel_name}
    Log To Console    ${result_data}
    Close Browser

calender_ctrl_new
    [Arguments]    ${agent}    ${cin}    ${cout}    ${din}    ${dout}    ${datein}    ${dateout}
    Click Element    //*[@id="frm"]/div[1]/div[2]/div[1]/div[2]/div/div/div/div/span
    ${no_of_click} =    month_select    ${din}
    ${weekin}=    Evaluate    '0'
    ${weekin}=    Convert To String    ${weekin}
    Log To Console    b
    FOR    ${i}    IN RANGE    7
        ${j}=    Evaluate    ${i}+1
        ${weekin}=    evaluate    '${j}'
        ${driver}=    Get WebElement    //*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[${j}]
        Log To Console    ${driver.text}
        @{temp}=    Split String    ${driver.text}
        Log to console    ${temp}
        ${f}=    Evaluate    0
        ${f}=    ccn_key3    ${j}    ${datein}    ${cin}    @{temp}
        Exit For Loop If    '${f}' == '1'
    END
    FOR    ${i}    IN RANGE    ${no_of_click}
        Click Element    //*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[1]
    END
    Log To Console    c
    month_select    ${dout}
    Sleep    1s
    Log To Console    d
    ${cout}=    Convert To Integer    ${cout}
    FOR    ${i}    IN RANGE    7
        ${j}=    Evaluate    ${i}+1
        ${driver}=    Get WebElement    //*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[${j}]
        Log To Console    ${driver.text}
        @{temp}=    Split String    ${driver.text}
        Log to console    ${temp}
        ${f}=    Evaluate    0
        ${f}=    ccn_key4    ${j}    ${dateout}    ${cout}    @{temp}
        ${weekout}=    evaluate    '${j}'
        Exit For Loop If    '${f}' == '1'
    END
    [Return]    ${weekin}    ${weekout}

month_select
    [Arguments]    ${din}
    @{checkin_date} =    Split String    ${din}    /
    ${cindate} =    Get From List    ${checkin_date}    0
    ${month} =    Get From List    ${checkin_date}    1
    ${year} =    Get From List    ${checkin_date}    2
    ${cindate} =    Convert To Integer    ${cindate}
    ${year} =    Convert To Integer    ${year}
    ${month} =    Convert To Integer    ${month}
    ${cur_month} =    Evaluate    '{dt.month}'.format(dt=datetime.datetime.now())    modules=datetime
    ${cur_year} =    Evaluate    '{dt.year}'.format(dt=datetime.datetime.now())    modules=datetime
    ${month_diff}=    Set Variable    0
    ${month_diff}=    Run Keyword If    '${month}' == '${cur_month}' and '${year}' == '${cur_year}'    month_select_key1    ${month}    ${cur_month}
    ...    ELSE    month_select_1    ${month}    ${cur_month}    ${year}    ${cur_year}
    Log To Console    ${month_diff}
    [Return]    ${month_diff}

month_select_key1
    [Arguments]    ${month}    ${cur_month}
    Log To Console    'm=cm and y=cr'    ${month_diff} =    ${month}-${cur_month}
    [Return]    ${month_diff}

month_select_key2
    [Arguments]    ${month}    ${cur_month}
    ${month_diff}=    Evaluate    ${month}-${cur_month}
    Log To Console    ${month}-${cur_month}
    FOR    ${i}    IN RANGE    ${month_diff}
        Click Element    //*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[2]
        Log To Console    INSIDE FOR
    END
    Log To Console    m-cm>0 and cy==yr
    Log To Console    ${month_diff}
    [Return]    ${month_diff}

month_select_key3
    Log To Console    Invalid dates
    Exit 0

month_select_key4
    [Arguments]    ${year}    ${cur_year}    ${month}    ${cur_month}
    Set Variable    ${no_of_click} =    12*(${year}-${cur_year})+(${month}-${cur_month})
    FOR    ${i}    IN RANGE    ${no_of_click}
        Click Element    //*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[2]/svg
    END
    Log To Console    m-cm>0 and cy<yr
    [Return]    {no_of_click}

month_select_key5
    [Arguments]    ${year}    ${cur_year}    ${cur_month}    ${month}
    ${no_of_click} =    Run Keyword If    ${year}<${cur_year}    month_select_key51
    ...    ELSE IF    ${year}>${cur_year}    month_select_key52    ${year}    ${cur_year}    ${cur_month}    ${month}
    [Return]    ${no_of_click}

month_select_key51
    Log To Console    Invalid dates
    exit 0

month_select_key52
    [Arguments]    ${year}    ${cur_year}    ${cur_month}    ${month}
    Set Variable    ${no_of_click} =    12*(${year}-${cur_year})-(${cur_month}-${month})
    FOR    ${i}    IN RANGE    ${no_of_click}
        Click Element    //*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[2]/svg
    END
    Log To Console    m<cm and cy<yr
    [Return]    ${no_of_click}

month_select_1
    [Arguments]    ${month}    ${cur_month}    ${year}    ${cur_year}
    ${month_diff} =    Run Keyword If    ${month}-${cur_month} >0    month_select_2    ${month}    ${cur_month}    ${year}    ${cur_year}
    ...    ELSE IF    ${month}<${cur_month}    month_select_key5    ${year}    ${cur_year}    ${cur_month}    ${month}
    [Return]    ${month_diff}

month_select_2
    [Arguments]    ${month}    ${cur_month}    ${year}    ${cur_year}
    ${month_diff} =    Run Keyword If    '${cur_year}'=='${year}'    month_select_key2    ${month}    ${cur_month}
    ...    ELSE IF    '${cur_year}'>'${year}'    month_select_key3
    ...    ELSE    '${cur_year}'<'${year}'    month_select_key4    ${year}    ${cur_year}    ${month}    ${cur_month}
    [Return]    ${month_diff}

ccn_key1
    [Arguments]    ${weekin}    ${datein}
    Click Element    //*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[ ${weekin}]/td[@data-date='${datein}']
    [Return]    ${1}

ccn_key2
    [Arguments]    ${weekout}    ${dateout}
    Click Element    //*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[${weekout}]/td[@data-date='${dateout}']
    [Return]    ${1}

ccn_key4
    [Arguments]    ${j}    ${dateout}    ${cout}    @{temp}
    ${f}=    evaluate    0
    FOR    ${k}    IN    @{temp}
        ${f}=    Run Keyword If    ${cout}==${k}    ccn_key2    ${j}    ${dateout}
        Exit For Loop If    '${f}' == '1'
    END
    [Return]    ${f}

ccn_key3
    [Arguments]    ${j}    ${datein}    ${cin}    @{temp}
    ${f}=    evaluate    0
    FOR    ${k}    IN    @{temp}
        ${f}=    Run Keyword If    ${cin} == ${k}    ccn_key1    ${j}    ${datein}
        Exit For Loop If    '${f}' == '1'
    END
    [Return]    ${f}

listing
    [Arguments]    ${hotel_id}
    ${listed}=    evaluate    0
    FOR    ${i}    IN RANGE    40
        Wait Until Element Is Visible    //*[@id='hotellist_inner']/div[@data-hotelid='${hotel_id}']    10
        ${j}=    evaluate    ${i}+1
        ${elem1}=    Get WebElement    //*[@id='hotellist_inner']/div[@data-hotelid='${hotel_id}']
        ${elem2}=    Get WebElement    //*[@id='hotellist_inner']/div[${j}]
        ${elem1}=    Convert To String    ${elem1}
        ${elem2}=    Convert To String    ${elem2}
        ${h}=    evaluate    '${elem1}'=='${elem2}'
        Log to console    ${h}
        ${f}=    Run Keyword If    ${h}    listing_key1    ${i}
        Exit For Loop If    ${f} !=None
    END
    [Return]    ${f}

listing_key1
    [Arguments]    ${i}
    ${listed}=    evaluate    ${i}+1
    [Return]    ${listed}

hotel_find
    [Arguments]    ${hotel_id}
    Click Element    //*[@id='hotellist_inner']/div[@data-hotelid='${hotel_id}']

data_scraping
    @{room_type}=    Create List
    @{room_price}=    Create List
    ${cnt}=    Get Length    ${room_typeids}
    FOR    ${i}    IN RANGE    ${cnt}
        @{n_list}=    Create List
        Append To List    ${room_price}    ${n_list}
        ${r_id}=    Get From List    ${room_typeids}    ${i}
        ${elem}=    Get Element Attribute    //*[@id='${r_id}']    data-room-name
        Log To Console    ${elem}
        Append To List    ${room_type}    ${elem}
        ${pr}=    datascraping_key1    ${i}
        Append To List    ${room_price[${i}]}    ${pr}
        Log To Console    ${room_price}
        Log To Console    ${room_type}
    END
    ${returnlist}=    Create List
    ${k}=    Get Length    ${room_type}
    FOR    ${i}    IN RANGE    ${k}
        Append To List    ${returnlist}    ${room_type[${i}]}
        Append To List    ${returnlist}    ${room_price[${i}]}
    END
    Log To Console    ${returnlist}
    [Return]    ${returnlist}

data_scraping_key1
    [Arguments]    ${i}
    ${len}=    Get Length    ${room_priceids}
    FOR    ${j}    IN RANGE    ${len}
        ${m}=    Get From List    ${room_typeids}    ${i}
        ${n}=    Split String    ${m}    _
        ${o}=    Get From List    ${n}    3
        ${p}=    Get From List    ${room_priceids}    ${j}
        ${q}=    Split String    ${p}    _
        ${r}=    Get From List    ${q}    0
        ${pr}=    Run Keyword If    ${o}==${r}    data_scraping_key11    ${j}
        Log To Console    ${pr}
        Exit For Loop If    ${o} == ${r}
    END
    [Return]    ${pr}

data_scraping_key11
    [Arguments]    ${j}
    ${p_id}=    Get From List    ${room_priceids}    ${j}
    ${a}=    Get WebElement    //*[@id='hprt_nos_select_${p_id}']
    ${a}=    Convert To String    ${a.text}
    ${a}=    String.Get Regexp Matches    ${a}    \(.*\)
    ${a}=    Get From List    ${a}    8
    ${a}=    String.Get Substring    ${a}    1
    ${a}=    String.Get Substring    ${a}    \    -1
    Log To Console    ${a}
    [Return]    ${a}
