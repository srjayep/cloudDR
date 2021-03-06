from django.conf.urls import url
from cloud.views import *
from django.conf import settings

urlpatterns = [
    url(r'^$', index),
    url(r'^test/$', test),
    url(r'^index/$', index),
    url(r'^get_dashboard_amchart_1/$', get_dashboard_amchart_1),
    url(r'^get_dashboard_amchart_2/$', get_dashboard_amchart_2),
    url(r'^get_dashboard_amchart_3/$', get_dashboard_amchart_3),
    url(r'^get_dashboard_amchart_4/$', get_dashboard_amchart_4),
    url(r'^not_display_jobs/$', not_display_jobs),
    url(r'^downloadlist/$', downloadlist),
    url(r'^download/$', download),
    url(r'^login/$', login),
    url(r'^userlogin/$', userlogin),
    url(r'^registUser/$', registUser),
    url(r'^forgetPassword/$', forgetPassword),
    url(r'^resetpassword/([0-9a-zA-Z]{8}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{12})/$',
        resetpassword),
    url(r'^reset/$', reset),
    url(r'^activate/$', activate),
    url(r'^useractivate/$', useractivate),
    url(r'^password/$', password),
    url(r'^userpassword/$', userpassword),
    url(r'^useredit/$', useredit),
    url(r'^usersave/$', usersave),
    url(r'^childuser/$', childuser),
    url(r'^childuserdata/$', childuserdata),
    url(r'^childusersave/$', childusersave),
    url(r'^childuserdel/$', childuserdel),
    url(r'^getallclients/$', getallclients),

    url(r'^script/$', script),
    url(r'^scriptdata/$', scriptdata),
    url(r'^scriptdel/$', scriptdel),
    url(r'^scriptsave/$', scriptsave),
    url(r'^scriptexport/$', scriptexport),
    url(r'^processscriptsave/$', processscriptsave),
    url(r'^get_scripts/$', get_scripts),
    url(r'^get_script_data/$', get_script_data),
    url(r'^remove_script/$', remove_script),

    url(r'^group/$', group),
    url(r'^groupsave/$', groupsave),
    url(r'^groupdel/$', groupdel),
    url(r'^getusers/$', getusers),
    url(r'^getselectedusers/$', getselectedusers),
    url(r'^groupsaveuser/$', groupsaveuser),

    url(r'^resourcepool/$', resourcepool),
    url(r'^resourcepooldata/$', resourcepooldata),
    url(r'^resourcepoolsave/$', resourcepoolsave),
    url(r'^resourcepooldel/$', resourcepooldel),
    url(r'^getvendorlist/$', getvendorlist),
    url(r'^computerresource/$', computerresource),
    url(r'^computerresourcedata/$', computerresourcedata),
    url(r'^computerresourcepooldata/$', computerresourcepooldata),
    url(r'^computerresourcesave/$', computerresourcesave),
    url(r'^computerresourcedel/$', computerresourcedel),
    url(r'^computerresourcepooldatafordrill/$', computerresourcepooldatafordrill),
    url(r'^computerresourcedatafordrill/$', computerresourcedatafordrill),

    url(r'^vmresource/$', vmresource),
    url(r'^vmresourcedata/$', vmresourcedata),
    url(r'^vmresourcepooldata/$', vmresourcepooldata),
    url(r'^vmresourcesave/$', vmresourcesave),
    url(r'^vmresourcedel/$', vmresourcedel),
    url(r'^vmresourcedestroy/$', vmresourcedestroy),
    url(r'^vmresourcepooldatafordrill/$', vmresourcepooldatafordrill),
    url(r'^vmresourcedatafordrill/$', vmresourcedatafordrill),

    url(r'^getvmresourcelist/$', getvmresourcelist),
    url(r'^vmlistmanage/', vmlistmanage),
    url(r'^vmlistmanagedata/$', vmlistmanagedata),
    url(r'^getvmtemplate/', getvmtemplate),

    url(r'^backupresource/$', backupresource),
    url(r'^backupresourcedata/$', backupresourcedata),
    url(r'^backupresourcepooldata/$', backupresourcepooldata),
    url(r'^backupresourcesave/$', backupresourcesave),
    url(r'^backupresourcedel/$', backupresourcedel),
    url(r'^getbackupcert/$', getbackupcert),

    url(r'^schduleresource/$', schduleresource),
    url(r'^schduleresourcedata/$', schduleresourcedata),
    url(r'^schduleresourcepooldata/$', schduleresourcepooldata),
    url(r'^schduleresourcesave/$', schduleresourcesave),
    url(r'^schduleresourcedel/$', schduleresourcedel),
    url(r'^getschdulecert/$', getschdulecert),

    url(r'^serverconfig/$', serverconfig),
    url(r'^serverconfigsave/$', serverconfigsave),
    url(r'^match/$', match),
    url(r'^matchdata/$', matchdata),
    url(r'^matching/$', matching),
    url(r'^matchsave/$', matchsave),

    url(r'^phyproconfig/$', phyproconfig),
    url(r'^phyproconfigdata/$', phyproconfigdata),
    url(r'^getphydataget/$', getphydataget),
    url(r'^phyproconfigsaveapp/$', phyproconfigsaveapp),
    url(r'^phyproconfigsavefile/$', phyproconfigsavefile),
    url(r'^phyproconfigsaveoracle/$', phyproconfigsaveoracle),
    url(r'^phyproconfigsavemssql/$', phyproconfigsavemssql),

    url(r'^vmproconfig/$', vmproconfig),
    url(r'^vmproconfigdata/$', vmproconfigdata),
    url(r'^vmproconfigsave/$', vmproconfigsave),
    url(r'^getvmlist/$', getvmlist),
    url(r'^get_dc/$', get_dc),
    url(r'^get_cluster/$', get_cluster),
    url(r'^clonevm/$', clonevm),
    url(r'^get_progress/$', get_progress),
    url(r'^vm_ipsave/$', vm_ipsave),
    url(r'^vm_hostsave/$', vm_hostsave),
    url(r'^vm_disksave/$', vm_disksave),
    url(r'^vm_installcvsave/$', vm_installcvsave),
    url(r'^registercvsave/$', registercvsave),
    # url(r'^vmlistmanagesave/$', vmlistmanagesave),
    url(r'^vmappsave/$', vmappsave),
    url(r'^vmproconfigdel/$', vmproconfigdel),
    url(r'^vmappdel/$', vmappdel),
    url(r'^rebootvm/$', rebootvm),
    url(r'^shutdownvm/$', shutdownvm),
    url(r'^poweronvm/$', poweronvm),
    url(r'^get_vm_state/$', get_vm_state),
    url(r'^get_dc_clt_from_pool/$', get_dc_clt_from_pool),

    url(r'^racproconfig/$', racproconfig),
    url(r'^racproconfigdata/$', racproconfigdata),
    url(r'^racproconfigsave/$', racproconfigsave),
    url(r'^racproconfigdel/$', racproconfigdel),

    url(r'^workflowset/$', workflowset),
    url(r'^getsetps/$', getsetps),
    url(r'^setpsave/$', setpsave),
    url(r'^disasterdrill/$', disasterdrill),
    url(r'^disasterdrilldata/$', disasterdrilldata),
    url(r'^manualrecovery/$', manualrecovery),
    url(r'^manualrecoverydata/$', manualrecoverydata),
    url(r'^oraclerecovery/(\d+)/$', oraclerecovery),
    url(r'^dooraclerecovery/$', dooraclerecovery),
    url(r'^oraclerecoverydata/$', oraclerecoverydata),

    url(r'^mssqlrecovery/(\d+)/$', mssqlrecovery),
    url(r'^domssqlrecovery/$', domssqlrecovery),
    url(r'^mssqlrecoverydata/$', mssqlrecoverydata),

    url(r'^filerecovery/(\d+)/$', filerecovery),
    url(r'^dofilerecovery/$', dofilerecovery),
    url(r'^filerecoverydata/$', filerecoverydata),
    url(r'^getfiletree/$', getfiletree),

    url(r'^vmrecovery/(\d+)/$', vmrecovery),
    url(r'^getproxylist/$', getproxylist),
    url(r'^dovmrecovery/$', dovmrecovery),
    url(r'^vmrecoverydata/$', vmrecoverydata),

    url(r'^addPhyClient/$', addPhyClient),
    url(r'^checkPhyClient/$', checkPhyClient),

    url(r'^report/$', report),
    url(r'^reportdata/$', reportdata),
    url(r'^creatprocessrun/$', creatprocessrun),
    url(r'^filecross/(\d+)/$', filecross),

    url(r'^filecrossprevious/$', filecrossprevious),
    url(r'^filecrossnext/$', filecrossnext),
    url(r'^getsinglevm/$', getsinglevm),
    url(r'^filecrossfinish/$', filecrossfinish),
    url(r'^get_current_scriptinfo/$', get_current_scriptinfo),
    url(r'^exec_script_by_hand/$', exec_script_by_hand),
    url(r'^ignore_current_script/$', ignore_current_script),

    url(r'^falconstorswitch/$', falconstorswitch),
    url(r'^falconstorswitchdata/$', falconstorswitchdata),
    url(r'^falconstorrun/$', falconstorrun),
    url(r'^falconstor/(\d+)/$', falconstor),
    url(r'^getrunsetps/$', getrunsetps),
    url(r'^falconstorcontinue/$', falconstorcontinue),
    url(r'^processsignsave/$', processsignsave),
    url(r'^custom_pdf_report/$', custom_pdf_report),
    url(r'^falconstorsearch/$', falconstorsearch),
    url(r'^falconstorsearchdata/$', falconstorsearchdata),

    url(r'^custom_step_tree/$', custom_step_tree),
    url(r'^step_tree_index/$', step_tree_index),
    url(r'^del_step/$', del_step),
    url(r'^move_step/$', move_step),
    url(r'^get_all_groups/$', get_all_groups),
]
