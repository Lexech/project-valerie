/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package valerie.tools;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.io.StringWriter;
import java.net.URL;
import java.net.URLConnection;
import org.jdom.Document;
import org.jdom.input.SAXBuilder;

/**
 *
 * @author Admin
 */
public class webgrabber {
    public Document getXML(URL url) {
        DebugOutput.printl(url.toString());
        //Serve the file
        Document doc = null;
        try {
            URLConnection urlc = url.openConnection();
            urlc.addRequestProperty("user-agent", "Firefox");
            InputStream in = urlc.getInputStream();

            StringWriter out = new StringWriter();
            byte[] buf = new byte[4 * 1024]; // 4K buffer
            int bytesRead;
            while ((bytesRead = in.read(buf)) != -1) {
                byte[] bufTrimmed = new byte[bytesRead];
                for(int j = 0; j < bytesRead; j++)
                    bufTrimmed[j] = buf[j];
                String fragment = new String(bufTrimmed);
                out.append(fragment);

            }
            String xmlString = out.toString();
            SAXBuilder builder = new SAXBuilder();
            StringReader xmlout = new StringReader(xmlString);
            doc = builder.build(xmlout);
        } catch (Exception ex) {
            System.out.printf("error %s\n", ex.getMessage());
        }

        DebugOutput.printl("<-");

        return doc;
    }

    public String getText(URL url) {

        DebugOutput.printl(url.toString());

        //Serve the file
        String doc = null;

        try {
            URLConnection urlc = url.openConnection();
            urlc.setRequestProperty("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.4) Gecko/2008102920 Firefox/3.0.4");
            /*InputStream in = urlc.getInputStream();

            StringWriter out = new StringWriter();
            byte[] buf = new byte[4 * 1024]; // 4K buffer
            int bytesRead;
            while ((bytesRead = in.read(buf)) != -1) {
                byte[] bufTrimmed = new byte[bytesRead];
                for(int j = 0; j < bytesRead; j++)
                    bufTrimmed[j] = buf[j];
                String fragment = new String(bufTrimmed);
                out.append(fragment);

            }
            doc = out.toString();*/
            BufferedReader in = new BufferedReader(new InputStreamReader(urlc.getInputStream()));

            StringWriter out = new StringWriter();
            String inputLine;
            while ( (inputLine = in.readLine()) != null)
            {
              out.append(inputLine);
            }
            in.close();
            doc = out.toString();
        } catch (Exception ex) {
            System.out.printf("error %s\n", ex.getMessage());
        }

        DebugOutput.printl("<-");

        return doc;
    }

    public void getFile(String surl, String SaveAs) {

        DebugOutput.printl(surl);

        try {
            URL url = new URL(surl);
            URLConnection urlc = url.openConnection();
            urlc.addRequestProperty("user-agent", "Firefox");
            InputStream in = urlc.getInputStream();

            byte[] buf = new byte[4 * 1024]; // 4K buffer
            int bytesRead;

            File outputfile = new File (SaveAs);
            FileOutputStream out = new FileOutputStream(outputfile);

            while ((bytesRead = in.read(buf)) != -1) {
                out.write(buf, 0, bytesRead);
            }
        } catch (Exception ex) {
            System.out.printf("error %s\n", ex.getMessage());
        }

        DebugOutput.printl("<-");

        return;
    }
}
