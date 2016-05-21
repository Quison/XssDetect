///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/statbmp.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/string.h>
#include <wx/sizer.h>
#include <wx/panel.h>
#include <wx/stattext.h>
#include <wx/slider.h>
#include <wx/statbox.h>
#include <wx/textctrl.h>
#include <wx/button.h>
#include <wx/grid.h>
#include <wx/notebook.h>
#include <wx/statusbr.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class XssDetectFrame
///////////////////////////////////////////////////////////////////////////////
class XssDetectFrame : public wxFrame 
{
	private:
	
	protected:
		wxPanel* logo_panel;
		wxStaticBitmap* logo_bitmap;
		wxNotebook* m_notebook4;
		wxPanel* setting_panel;
		wxPanel* thread_ctrl_panel;
		wxStaticText* spider_thread_num_staticText;
		wxSlider* spider_thread_num_slider;
		wxStaticText* m_staticText_spider_unit;
		wxStaticText* m_staticText_space;
		wxStaticText* check_thread_num_staticText;
		wxSlider* check_thread_num_slider;
		wxStaticText* m_staticText_check_unit;
		wxPanel* setting_login_info_panel;
		wxPanel* setting_cookie_panel;
		wxStaticText* login_url_staticText;
		wxTextCtrl* login_url_textCtrl;
		wxStaticText* cookie_staticText;
		wxTextCtrl* cookie_textCtrl;
		wxPanel* setting_username_panel;
		wxStaticText* username_key_staticText;
		wxTextCtrl* username_key_textCtrl;
		wxStaticText* username_value_staticText1;
		wxStaticText* username_value_staticText;
		wxTextCtrl* username_value_textCtr;
		wxPanel* setting_password_panel;
		wxStaticText* password_key_staticText;
		wxTextCtrl* password_key_textCtrl;
		wxStaticText* username_value_staticText11;
		wxStaticText* password_value_staticText;
		wxTextCtrl* password_value_textCtr;
		wxPanel* setting_vercode_panel;
		wxStaticText* vercode_key_staticText;
		wxTextCtrl* vercode_key_textCtrl;
		wxStaticText* username_value_staticText111;
		wxStaticText* vercode_value_staticText;
		wxTextCtrl* vercode_value_textCtr;
		wxPanel* setting_login_info_ctrl_panel;
		wxStaticText* vercode_staticText;
		wxTextCtrl* vercode_textCtrl;
		wxStaticBitmap* vercode_bitmap;
		wxButton* get_vercode_button;
		wxButton* login_button;
		wxPanel* setting_payload_panel;
		wxPanel* setting_payload_text_panel;
		wxPanel* payload_text_panel;
		wxStaticText* payload_staticText;
		wxTextCtrl* payload_textCtrl;
		wxPanel* exclude_url_panel;
		wxStaticText* exclude_url_staticText;
		wxTextCtrl* exclude_url_textCtrl;
		wxPanel* save_info_panel;
		wxStaticText* save_info_staticText;
		wxButton* save_payload_button;
		wxStaticText* save_info_staticText1;
		wxButton* m_button6;
		wxPanel* spider_panel;
		wxPanel* spider_ctrl_panel;
		wxStaticText* seed_url_label;
		wxTextCtrl* seed_url_text;
		wxStaticText* m_staticText29;
		wxStaticText* crawl_depth_staticText;
		wxTextCtrl* crawl_depth_textCtrl;
		wxButton* start_crawling_button;
		wxPanel* spider_show_panel;
		wxGrid* spider_grid;
		wxPanel* check_panel;
		wxPanel* check_ctrl_panel;
		wxStaticText* reflect_check_staticText;
		wxStaticText* reflect_checking_url;
		wxButton* start_check_button;
		wxPanel* check_show_panel;
		wxGrid* check_grid;
		wxStatusBar* statusBar;
		
		// Virtual event handlers, overide them in your derived class
		virtual void OnSpiderThreadNumScroll( wxScrollEvent& event ) { event.Skip(); }
		virtual void OnCheckThreadNumScroll( wxScrollEvent& event ) { event.Skip(); }
		virtual void OnGetVercodeButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void OnLoginButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void OnSavePayloadButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void OnSaveSettingInfoButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void OnBeginCrawlingButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void OnBeginCheckButtonClick( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		XssDetectFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("Xss Detector"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 800,747 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~XssDetectFrame();
	
};

#endif //__NONAME_H__
