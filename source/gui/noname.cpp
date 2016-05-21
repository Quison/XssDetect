///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

XssDetectFrame::XssDetectFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxBoxSizer* main_bSizer;
	main_bSizer = new wxBoxSizer( wxVERTICAL );
	
	logo_panel = new wxPanel( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* logo_bSizer;
	logo_bSizer = new wxBoxSizer( wxVERTICAL );
	
	logo_bitmap = new wxStaticBitmap( logo_panel, wxID_ANY, wxBitmap( wxT("images/logo.jpg"), wxBITMAP_TYPE_ANY ), wxDefaultPosition, wxDefaultSize, 0 );
	logo_bSizer->Add( logo_bitmap, 2, wxALIGN_CENTER_VERTICAL|wxALL|wxEXPAND, 5 );
	
	
	logo_panel->SetSizer( logo_bSizer );
	logo_panel->Layout();
	logo_bSizer->Fit( logo_panel );
	main_bSizer->Add( logo_panel, 3, wxEXPAND | wxALL, 5 );
	
	m_notebook4 = new wxNotebook( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	setting_panel = new wxPanel( m_notebook4, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* setting_bSizer;
	setting_bSizer = new wxBoxSizer( wxVERTICAL );
	
	thread_ctrl_panel = new wxPanel( setting_panel, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxStaticBoxSizer* thread_ctrl_sbSizer;
	thread_ctrl_sbSizer = new wxStaticBoxSizer( new wxStaticBox( thread_ctrl_panel, wxID_ANY, wxT("系统线程设置") ), wxHORIZONTAL );
	
	spider_thread_num_staticText = new wxStaticText( thread_ctrl_sbSizer->GetStaticBox(), wxID_ANY, wxT("爬虫线程数量（0~100）："), wxDefaultPosition, wxDefaultSize, 0 );
	spider_thread_num_staticText->Wrap( -1 );
	thread_ctrl_sbSizer->Add( spider_thread_num_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	spider_thread_num_slider = new wxSlider( thread_ctrl_sbSizer->GetStaticBox(), wxID_ANY, 10, 0, 100, wxDefaultPosition, wxDefaultSize, wxSL_HORIZONTAL );
	thread_ctrl_sbSizer->Add( spider_thread_num_slider, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	m_staticText_spider_unit = new wxStaticText( thread_ctrl_sbSizer->GetStaticBox(), wxID_ANY, wxT("10"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText_spider_unit->Wrap( -1 );
	thread_ctrl_sbSizer->Add( m_staticText_spider_unit, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	m_staticText_space = new wxStaticText( thread_ctrl_sbSizer->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0, wxT("df") );
	m_staticText_space->Wrap( -1 );
	thread_ctrl_sbSizer->Add( m_staticText_space, 1, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	check_thread_num_staticText = new wxStaticText( thread_ctrl_sbSizer->GetStaticBox(), wxID_ANY, wxT("检测线程数量（0~100）："), wxDefaultPosition, wxDefaultSize, 0 );
	check_thread_num_staticText->Wrap( -1 );
	thread_ctrl_sbSizer->Add( check_thread_num_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	check_thread_num_slider = new wxSlider( thread_ctrl_sbSizer->GetStaticBox(), wxID_ANY, 10, 0, 100, wxDefaultPosition, wxDefaultSize, wxSL_HORIZONTAL );
	thread_ctrl_sbSizer->Add( check_thread_num_slider, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	m_staticText_check_unit = new wxStaticText( thread_ctrl_sbSizer->GetStaticBox(), wxID_ANY, wxT("10"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText_check_unit->Wrap( -1 );
	thread_ctrl_sbSizer->Add( m_staticText_check_unit, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	
	thread_ctrl_panel->SetSizer( thread_ctrl_sbSizer );
	thread_ctrl_panel->Layout();
	thread_ctrl_sbSizer->Fit( thread_ctrl_panel );
	setting_bSizer->Add( thread_ctrl_panel, 1, wxEXPAND | wxALL, 5 );
	
	setting_login_info_panel = new wxPanel( setting_panel, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxStaticBoxSizer* setting_login_info_sbSizer;
	setting_login_info_sbSizer = new wxStaticBoxSizer( new wxStaticBox( setting_login_info_panel, wxID_ANY, wxT("HTTP授权信息") ), wxVERTICAL );
	
	setting_cookie_panel = new wxPanel( setting_login_info_sbSizer->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* setting_cookie_bSizer;
	setting_cookie_bSizer = new wxBoxSizer( wxHORIZONTAL );
	
	login_url_staticText = new wxStaticText( setting_cookie_panel, wxID_ANY, wxT("登录链接："), wxDefaultPosition, wxDefaultSize, 0 );
	login_url_staticText->Wrap( -1 );
	setting_cookie_bSizer->Add( login_url_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	login_url_textCtrl = new wxTextCtrl( setting_cookie_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	setting_cookie_bSizer->Add( login_url_textCtrl, 1, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	cookie_staticText = new wxStaticText( setting_cookie_panel, wxID_ANY, wxT("Cookie："), wxDefaultPosition, wxDefaultSize, 0 );
	cookie_staticText->Wrap( -1 );
	setting_cookie_bSizer->Add( cookie_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	cookie_textCtrl = new wxTextCtrl( setting_cookie_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	setting_cookie_bSizer->Add( cookie_textCtrl, 1, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	
	setting_cookie_panel->SetSizer( setting_cookie_bSizer );
	setting_cookie_panel->Layout();
	setting_cookie_bSizer->Fit( setting_cookie_panel );
	setting_login_info_sbSizer->Add( setting_cookie_panel, 1, wxEXPAND | wxALL, 5 );
	
	setting_username_panel = new wxPanel( setting_login_info_sbSizer->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* setting_username_bSizer;
	setting_username_bSizer = new wxBoxSizer( wxHORIZONTAL );
	
	username_key_staticText = new wxStaticText( setting_username_panel, wxID_ANY, wxT("username key："), wxDefaultPosition, wxDefaultSize, 0 );
	username_key_staticText->Wrap( -1 );
	setting_username_bSizer->Add( username_key_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	username_key_textCtrl = new wxTextCtrl( setting_username_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	setting_username_bSizer->Add( username_key_textCtrl, 3, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	username_value_staticText1 = new wxStaticText( setting_username_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	username_value_staticText1->Wrap( -1 );
	setting_username_bSizer->Add( username_value_staticText1, 1, wxALL, 5 );
	
	username_value_staticText = new wxStaticText( setting_username_panel, wxID_ANY, wxT("username value："), wxDefaultPosition, wxDefaultSize, 0 );
	username_value_staticText->Wrap( -1 );
	setting_username_bSizer->Add( username_value_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	username_value_textCtr = new wxTextCtrl( setting_username_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	setting_username_bSizer->Add( username_value_textCtr, 3, wxALL, 5 );
	
	
	setting_username_panel->SetSizer( setting_username_bSizer );
	setting_username_panel->Layout();
	setting_username_bSizer->Fit( setting_username_panel );
	setting_login_info_sbSizer->Add( setting_username_panel, 1, wxEXPAND | wxALL, 5 );
	
	setting_password_panel = new wxPanel( setting_login_info_sbSizer->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* setting_username_bSizer1;
	setting_username_bSizer1 = new wxBoxSizer( wxHORIZONTAL );
	
	password_key_staticText = new wxStaticText( setting_password_panel, wxID_ANY, wxT("password key："), wxDefaultPosition, wxDefaultSize, 0 );
	password_key_staticText->Wrap( -1 );
	setting_username_bSizer1->Add( password_key_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	password_key_textCtrl = new wxTextCtrl( setting_password_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	setting_username_bSizer1->Add( password_key_textCtrl, 3, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	username_value_staticText11 = new wxStaticText( setting_password_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	username_value_staticText11->Wrap( -1 );
	setting_username_bSizer1->Add( username_value_staticText11, 1, wxALL, 5 );
	
	password_value_staticText = new wxStaticText( setting_password_panel, wxID_ANY, wxT("password value："), wxDefaultPosition, wxDefaultSize, 0 );
	password_value_staticText->Wrap( -1 );
	setting_username_bSizer1->Add( password_value_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	password_value_textCtr = new wxTextCtrl( setting_password_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	setting_username_bSizer1->Add( password_value_textCtr, 3, wxALL, 5 );
	
	
	setting_password_panel->SetSizer( setting_username_bSizer1 );
	setting_password_panel->Layout();
	setting_username_bSizer1->Fit( setting_password_panel );
	setting_login_info_sbSizer->Add( setting_password_panel, 1, wxEXPAND | wxALL, 5 );
	
	setting_vercode_panel = new wxPanel( setting_login_info_sbSizer->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* setting_username_bSizer11;
	setting_username_bSizer11 = new wxBoxSizer( wxHORIZONTAL );
	
	vercode_key_staticText = new wxStaticText( setting_vercode_panel, wxID_ANY, wxT("vercode key："), wxDefaultPosition, wxDefaultSize, 0 );
	vercode_key_staticText->Wrap( -1 );
	setting_username_bSizer11->Add( vercode_key_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	vercode_key_textCtrl = new wxTextCtrl( setting_vercode_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	setting_username_bSizer11->Add( vercode_key_textCtrl, 3, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	username_value_staticText111 = new wxStaticText( setting_vercode_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	username_value_staticText111->Wrap( -1 );
	setting_username_bSizer11->Add( username_value_staticText111, 1, wxALL, 5 );
	
	vercode_value_staticText = new wxStaticText( setting_vercode_panel, wxID_ANY, wxT("vercode value："), wxDefaultPosition, wxDefaultSize, 0 );
	vercode_value_staticText->Wrap( -1 );
	setting_username_bSizer11->Add( vercode_value_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	vercode_value_textCtr = new wxTextCtrl( setting_vercode_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	setting_username_bSizer11->Add( vercode_value_textCtr, 3, wxALL, 5 );
	
	
	setting_vercode_panel->SetSizer( setting_username_bSizer11 );
	setting_vercode_panel->Layout();
	setting_username_bSizer11->Fit( setting_vercode_panel );
	setting_login_info_sbSizer->Add( setting_vercode_panel, 1, wxEXPAND | wxALL, 5 );
	
	setting_login_info_ctrl_panel = new wxPanel( setting_login_info_sbSizer->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* settinglogin_bSizer;
	settinglogin_bSizer = new wxBoxSizer( wxHORIZONTAL );
	
	vercode_staticText = new wxStaticText( setting_login_info_ctrl_panel, wxID_ANY, wxT("验证码链接："), wxDefaultPosition, wxDefaultSize, 0 );
	vercode_staticText->Wrap( -1 );
	settinglogin_bSizer->Add( vercode_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	vercode_textCtrl = new wxTextCtrl( setting_login_info_ctrl_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	settinglogin_bSizer->Add( vercode_textCtrl, 3, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	vercode_bitmap = new wxStaticBitmap( setting_login_info_ctrl_panel, wxID_ANY, wxNullBitmap, wxDefaultPosition, wxDefaultSize, 0 );
	settinglogin_bSizer->Add( vercode_bitmap, 1, wxALIGN_CENTER_VERTICAL|wxALL|wxEXPAND, 5 );
	
	get_vercode_button = new wxButton( setting_login_info_ctrl_panel, wxID_ANY, wxT("获取验证码"), wxDefaultPosition, wxDefaultSize, 0 );
	settinglogin_bSizer->Add( get_vercode_button, 1, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	login_button = new wxButton( setting_login_info_ctrl_panel, wxID_ANY, wxT("登录"), wxDefaultPosition, wxDefaultSize, 0 );
	settinglogin_bSizer->Add( login_button, 1, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	
	setting_login_info_ctrl_panel->SetSizer( settinglogin_bSizer );
	setting_login_info_ctrl_panel->Layout();
	settinglogin_bSizer->Fit( setting_login_info_ctrl_panel );
	setting_login_info_sbSizer->Add( setting_login_info_ctrl_panel, 1, wxEXPAND | wxALL, 5 );
	
	
	setting_login_info_panel->SetSizer( setting_login_info_sbSizer );
	setting_login_info_panel->Layout();
	setting_login_info_sbSizer->Fit( setting_login_info_panel );
	setting_bSizer->Add( setting_login_info_panel, 5, wxEXPAND | wxALL, 5 );
	
	setting_payload_panel = new wxPanel( setting_panel, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxStaticBoxSizer* setting_payload_sbSizer;
	setting_payload_sbSizer = new wxStaticBoxSizer( new wxStaticBox( setting_payload_panel, wxID_ANY, wxT("自定义信息") ), wxHORIZONTAL );
	
	setting_payload_text_panel = new wxPanel( setting_payload_sbSizer->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* setting_payload_text_bSizer;
	setting_payload_text_bSizer = new wxBoxSizer( wxVERTICAL );
	
	payload_text_panel = new wxPanel( setting_payload_text_panel, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* payload_text_bSizer;
	payload_text_bSizer = new wxBoxSizer( wxVERTICAL );
	
	payload_staticText = new wxStaticText( payload_text_panel, wxID_ANY, wxT("自定义向量："), wxDefaultPosition, wxDefaultSize, 0 );
	payload_staticText->Wrap( -1 );
	payload_text_bSizer->Add( payload_staticText, 0, wxALL, 5 );
	
	payload_textCtrl = new wxTextCtrl( payload_text_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_MULTILINE );
	payload_text_bSizer->Add( payload_textCtrl, 1, wxALL|wxEXPAND, 5 );
	
	
	payload_text_panel->SetSizer( payload_text_bSizer );
	payload_text_panel->Layout();
	payload_text_bSizer->Fit( payload_text_panel );
	setting_payload_text_bSizer->Add( payload_text_panel, 3, wxEXPAND | wxALL, 5 );
	
	exclude_url_panel = new wxPanel( setting_payload_text_panel, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* exclude_url_bSizer;
	exclude_url_bSizer = new wxBoxSizer( wxHORIZONTAL );
	
	exclude_url_staticText = new wxStaticText( exclude_url_panel, wxID_ANY, wxT("排除的URL："), wxDefaultPosition, wxDefaultSize, 0 );
	exclude_url_staticText->Wrap( -1 );
	exclude_url_bSizer->Add( exclude_url_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	exclude_url_textCtrl = new wxTextCtrl( exclude_url_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	exclude_url_bSizer->Add( exclude_url_textCtrl, 1, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	
	exclude_url_panel->SetSizer( exclude_url_bSizer );
	exclude_url_panel->Layout();
	exclude_url_bSizer->Fit( exclude_url_panel );
	setting_payload_text_bSizer->Add( exclude_url_panel, 1, wxEXPAND | wxALL, 5 );
	
	
	setting_payload_text_panel->SetSizer( setting_payload_text_bSizer );
	setting_payload_text_panel->Layout();
	setting_payload_text_bSizer->Fit( setting_payload_text_panel );
	setting_payload_sbSizer->Add( setting_payload_text_panel, 3, wxEXPAND | wxALL, 5 );
	
	save_info_panel = new wxPanel( setting_payload_sbSizer->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* save_info_bSizer;
	save_info_bSizer = new wxBoxSizer( wxVERTICAL );
	
	save_info_staticText = new wxStaticText( save_info_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	save_info_staticText->Wrap( -1 );
	save_info_bSizer->Add( save_info_staticText, 1, wxALL, 5 );
	
	save_payload_button = new wxButton( save_info_panel, wxID_ANY, wxT("添加PAYLOAD"), wxDefaultPosition, wxDefaultSize, 0 );
	save_info_bSizer->Add( save_payload_button, 0, wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL|wxEXPAND, 5 );
	
	save_info_staticText1 = new wxStaticText( save_info_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	save_info_staticText1->Wrap( -1 );
	save_info_bSizer->Add( save_info_staticText1, 1, wxALL, 5 );
	
	m_button6 = new wxButton( save_info_panel, wxID_ANY, wxT("保存系统设置"), wxDefaultPosition, wxDefaultSize, 0 );
	save_info_bSizer->Add( m_button6, 0, wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL|wxEXPAND, 5 );
	
	
	save_info_panel->SetSizer( save_info_bSizer );
	save_info_panel->Layout();
	save_info_bSizer->Fit( save_info_panel );
	setting_payload_sbSizer->Add( save_info_panel, 1, wxEXPAND | wxALL, 5 );
	
	
	setting_payload_panel->SetSizer( setting_payload_sbSizer );
	setting_payload_panel->Layout();
	setting_payload_sbSizer->Fit( setting_payload_panel );
	setting_bSizer->Add( setting_payload_panel, 3, wxEXPAND | wxALL, 5 );
	
	
	setting_panel->SetSizer( setting_bSizer );
	setting_panel->Layout();
	setting_bSizer->Fit( setting_panel );
	m_notebook4->AddPage( setting_panel, wxT("系统设置"), false );
	spider_panel = new wxPanel( m_notebook4, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* spider_bSizer;
	spider_bSizer = new wxBoxSizer( wxVERTICAL );
	
	spider_ctrl_panel = new wxPanel( spider_panel, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* spider_ctrl_bSizer;
	spider_ctrl_bSizer = new wxBoxSizer( wxHORIZONTAL );
	
	seed_url_label = new wxStaticText( spider_ctrl_panel, wxID_ANY, wxT("种子连接："), wxDefaultPosition, wxDefaultSize, 0 );
	seed_url_label->Wrap( -1 );
	spider_ctrl_bSizer->Add( seed_url_label, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	seed_url_text = new wxTextCtrl( spider_ctrl_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	spider_ctrl_bSizer->Add( seed_url_text, 7, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	m_staticText29 = new wxStaticText( spider_ctrl_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText29->Wrap( -1 );
	spider_ctrl_bSizer->Add( m_staticText29, 1, wxALL, 5 );
	
	crawl_depth_staticText = new wxStaticText( spider_ctrl_panel, wxID_ANY, wxT("爬取深度："), wxDefaultPosition, wxDefaultSize, 0 );
	crawl_depth_staticText->Wrap( -1 );
	spider_ctrl_bSizer->Add( crawl_depth_staticText, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	crawl_depth_textCtrl = new wxTextCtrl( spider_ctrl_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	spider_ctrl_bSizer->Add( crawl_depth_textCtrl, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	start_crawling_button = new wxButton( spider_ctrl_panel, wxID_ANY, wxT("开始爬取"), wxDefaultPosition, wxDefaultSize, 0 );
	spider_ctrl_bSizer->Add( start_crawling_button, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	
	spider_ctrl_panel->SetSizer( spider_ctrl_bSizer );
	spider_ctrl_panel->Layout();
	spider_ctrl_bSizer->Fit( spider_ctrl_panel );
	spider_bSizer->Add( spider_ctrl_panel, 1, wxALL|wxEXPAND, 5 );
	
	spider_show_panel = new wxPanel( spider_panel, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* spider_grid_bSizer;
	spider_grid_bSizer = new wxBoxSizer( wxVERTICAL );
	
	spider_grid = new wxGrid( spider_show_panel, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	
	// Grid
	spider_grid->CreateGrid( 10, 4 );
	spider_grid->EnableEditing( true );
	spider_grid->EnableGridLines( true );
	spider_grid->EnableDragGridSize( false );
	spider_grid->SetMargins( 0, 0 );
	
	// Columns
	spider_grid->SetColSize( 0, 64 );
	spider_grid->SetColSize( 1, 446 );
	spider_grid->SetColSize( 2, 80 );
	spider_grid->SetColSize( 3, 78 );
	spider_grid->EnableDragColMove( false );
	spider_grid->EnableDragColSize( true );
	spider_grid->SetColLabelSize( 30 );
	spider_grid->SetColLabelValue( 0, wxT("线程名") );
	spider_grid->SetColLabelValue( 1, wxT("URL") );
	spider_grid->SetColLabelValue( 2, wxT("请求类型") );
	spider_grid->SetColLabelValue( 3, wxT("深度") );
	spider_grid->SetColLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Rows
	spider_grid->EnableDragRowSize( true );
	spider_grid->SetRowLabelSize( 80 );
	spider_grid->SetRowLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Label Appearance
	
	// Cell Defaults
	spider_grid->SetDefaultCellAlignment( wxALIGN_LEFT, wxALIGN_TOP );
	spider_grid_bSizer->Add( spider_grid, 1, wxALL|wxEXPAND, 5 );
	
	
	spider_show_panel->SetSizer( spider_grid_bSizer );
	spider_show_panel->Layout();
	spider_grid_bSizer->Fit( spider_show_panel );
	spider_bSizer->Add( spider_show_panel, 6, wxEXPAND | wxALL, 5 );
	
	
	spider_panel->SetSizer( spider_bSizer );
	spider_panel->Layout();
	spider_bSizer->Fit( spider_panel );
	m_notebook4->AddPage( spider_panel, wxT("网络爬虫"), false );
	check_panel = new wxPanel( m_notebook4, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* check_bSizer;
	check_bSizer = new wxBoxSizer( wxVERTICAL );
	
	check_ctrl_panel = new wxPanel( check_panel, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* reflected_check_bSizer;
	reflected_check_bSizer = new wxBoxSizer( wxHORIZONTAL );
	
	reflect_check_staticText = new wxStaticText( check_ctrl_panel, wxID_ANY, wxT("反射型XSS检测："), wxDefaultPosition, wxDefaultSize, 0 );
	reflect_check_staticText->Wrap( -1 );
	reflected_check_bSizer->Add( reflect_check_staticText, 0, wxALL, 5 );
	
	reflect_checking_url = new wxStaticText( check_ctrl_panel, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	reflect_checking_url->Wrap( -1 );
	reflected_check_bSizer->Add( reflect_checking_url, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 );
	
	start_check_button = new wxButton( check_ctrl_panel, wxID_ANY, wxT("开始检测"), wxDefaultPosition, wxDefaultSize, 0 );
	reflected_check_bSizer->Add( start_check_button, 0, wxALL, 5 );
	
	
	check_ctrl_panel->SetSizer( reflected_check_bSizer );
	check_ctrl_panel->Layout();
	reflected_check_bSizer->Fit( check_ctrl_panel );
	check_bSizer->Add( check_ctrl_panel, 1, wxEXPAND | wxALL, 5 );
	
	check_show_panel = new wxPanel( check_panel, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* check_show_bSizer;
	check_show_bSizer = new wxBoxSizer( wxVERTICAL );
	
	check_grid = new wxGrid( check_show_panel, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	
	// Grid
	check_grid->CreateGrid( 10, 3 );
	check_grid->EnableEditing( false );
	check_grid->EnableGridLines( true );
	check_grid->EnableDragGridSize( false );
	check_grid->SetMargins( 0, 0 );
	
	// Columns
	check_grid->SetColSize( 0, 80 );
	check_grid->SetColSize( 1, 422 );
	check_grid->SetColSize( 2, 163 );
	check_grid->EnableDragColMove( false );
	check_grid->EnableDragColSize( true );
	check_grid->SetColLabelSize( 30 );
	check_grid->SetColLabelValue( 0, wxT("XSS漏洞类型") );
	check_grid->SetColLabelValue( 1, wxT("存在漏洞的URL") );
	check_grid->SetColLabelValue( 2, wxT("PAYLOAD") );
	check_grid->SetColLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Rows
	check_grid->EnableDragRowSize( true );
	check_grid->SetRowLabelSize( 80 );
	check_grid->SetRowLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Label Appearance
	
	// Cell Defaults
	check_grid->SetDefaultCellAlignment( wxALIGN_LEFT, wxALIGN_TOP );
	check_show_bSizer->Add( check_grid, 1, wxALL|wxEXPAND, 5 );
	
	
	check_show_panel->SetSizer( check_show_bSizer );
	check_show_panel->Layout();
	check_show_bSizer->Fit( check_show_panel );
	check_bSizer->Add( check_show_panel, 4, wxEXPAND | wxALL, 5 );
	
	
	check_panel->SetSizer( check_bSizer );
	check_panel->Layout();
	check_bSizer->Fit( check_panel );
	m_notebook4->AddPage( check_panel, wxT("XSS 检测"), true );
	
	main_bSizer->Add( m_notebook4, 3, wxEXPAND | wxALL, 5 );
	
	
	this->SetSizer( main_bSizer );
	this->Layout();
	statusBar = this->CreateStatusBar( 1, wxST_SIZEGRIP, wxID_ANY );
	
	this->Centre( wxBOTH );
	
	// Connect Events
	spider_thread_num_slider->Connect( wxEVT_SCROLL_TOP, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Connect( wxEVT_SCROLL_BOTTOM, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Connect( wxEVT_SCROLL_LINEUP, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Connect( wxEVT_SCROLL_LINEDOWN, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Connect( wxEVT_SCROLL_PAGEUP, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Connect( wxEVT_SCROLL_PAGEDOWN, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Connect( wxEVT_SCROLL_THUMBTRACK, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Connect( wxEVT_SCROLL_THUMBRELEASE, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Connect( wxEVT_SCROLL_CHANGED, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	check_thread_num_slider->Connect( wxEVT_SCROLL_TOP, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Connect( wxEVT_SCROLL_BOTTOM, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Connect( wxEVT_SCROLL_LINEUP, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Connect( wxEVT_SCROLL_LINEDOWN, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Connect( wxEVT_SCROLL_PAGEUP, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Connect( wxEVT_SCROLL_PAGEDOWN, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Connect( wxEVT_SCROLL_THUMBTRACK, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Connect( wxEVT_SCROLL_THUMBRELEASE, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Connect( wxEVT_SCROLL_CHANGED, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	get_vercode_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnGetVercodeButtonClick ), NULL, this );
	login_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnLoginButtonClick ), NULL, this );
	save_payload_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnSavePayloadButtonClick ), NULL, this );
	m_button6->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnSaveSettingInfoButtonClick ), NULL, this );
	start_crawling_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnBeginCrawlingButtonClick ), NULL, this );
	start_check_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnBeginCheckButtonClick ), NULL, this );
}

XssDetectFrame::~XssDetectFrame()
{
	// Disconnect Events
	spider_thread_num_slider->Disconnect( wxEVT_SCROLL_TOP, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Disconnect( wxEVT_SCROLL_BOTTOM, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Disconnect( wxEVT_SCROLL_LINEUP, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Disconnect( wxEVT_SCROLL_LINEDOWN, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Disconnect( wxEVT_SCROLL_PAGEUP, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Disconnect( wxEVT_SCROLL_PAGEDOWN, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Disconnect( wxEVT_SCROLL_THUMBTRACK, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Disconnect( wxEVT_SCROLL_THUMBRELEASE, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	spider_thread_num_slider->Disconnect( wxEVT_SCROLL_CHANGED, wxScrollEventHandler( XssDetectFrame::OnSpiderThreadNumScroll ), NULL, this );
	check_thread_num_slider->Disconnect( wxEVT_SCROLL_TOP, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Disconnect( wxEVT_SCROLL_BOTTOM, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Disconnect( wxEVT_SCROLL_LINEUP, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Disconnect( wxEVT_SCROLL_LINEDOWN, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Disconnect( wxEVT_SCROLL_PAGEUP, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Disconnect( wxEVT_SCROLL_PAGEDOWN, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Disconnect( wxEVT_SCROLL_THUMBTRACK, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Disconnect( wxEVT_SCROLL_THUMBRELEASE, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	check_thread_num_slider->Disconnect( wxEVT_SCROLL_CHANGED, wxScrollEventHandler( XssDetectFrame::OnCheckThreadNumScroll ), NULL, this );
	get_vercode_button->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnGetVercodeButtonClick ), NULL, this );
	login_button->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnLoginButtonClick ), NULL, this );
	save_payload_button->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnSavePayloadButtonClick ), NULL, this );
	m_button6->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnSaveSettingInfoButtonClick ), NULL, this );
	start_crawling_button->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnBeginCrawlingButtonClick ), NULL, this );
	start_check_button->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( XssDetectFrame::OnBeginCheckButtonClick ), NULL, this );
	
}
