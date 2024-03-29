/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package valerie.controller;

import java.io.File;
import java.net.URL;
import valerie.MediaInfo;
import valerie.provider.TheMovieDbProvider;
import valerie.provider.TheTvDbProvider;
import valerie.tools.WebGrabber;

/**
 *
 * @author i7
 */
public class Arts {

    public void download(MediaInfo eInfo) {
        if(eInfo.isMovie) {
            if(eInfo.Poster.length() == 0 || eInfo.Backdrop.length() == 0)
                new TheMovieDbProvider().getArtById(eInfo);

            if(eInfo.Poster.length() > 0) {
                if(new File("converted/" + eInfo.ImdbId + "_poster.png").isFile() == false) {
                    String url = WebGrabber.getText("http://val.duckbox.info/cgi-bin/convert.py?" + eInfo.ImdbId + ";poster;" + eInfo.Poster);
                    if(url != null && !url.equals("NONE")) {
                        WebGrabber.getFile("http://val.duckbox.info" + url, "converted/" + eInfo.ImdbId + "_poster.png");
                    }
                }
            }

            if(eInfo.Backdrop.length() > 0) {
                if(     new File("converted/" + eInfo.ImdbId + "_backdrop.m1v").isFile() == false ||
                        new File("converted/" + eInfo.ImdbId + "_backdrop_low.m1v").isFile() == false ||
                        new File("converted/" + eInfo.ImdbId + "_backdrop.png").isFile() == false) {
                    String url = WebGrabber.getText("http://val.duckbox.info/cgi-bin/convert.py?" + eInfo.ImdbId + ";backdrop;" + eInfo.Backdrop);
                    if(url != null && !url.equals("NONE")) {
                        String[] urls = url.split("<br />");
                        WebGrabber.getFile("http://val.duckbox.info" + urls[0], "converted/" + eInfo.ImdbId + "_backdrop.m1v");
                        WebGrabber.getFile("http://val.duckbox.info" + urls[1], "converted/" + eInfo.ImdbId + "_backdrop_low.m1v");
                        WebGrabber.getFile("http://val.duckbox.info" + urls[2], "converted/" + eInfo.ImdbId + "_backdrop.png");
                    }
                }
            }
        }
        else if(eInfo.isSerie) {
            if(eInfo.Poster.length() == 0 || eInfo.Backdrop.length() == 0)
                new TheTvDbProvider().getArtById(eInfo);

            if(eInfo.Poster.length() > 0) {
                if(new File("converted/" + eInfo.TheTvDbId + "_poster.png").isFile() == false) {
                    String url = WebGrabber.getText("http://val.duckbox.info/cgi-bin/convert.py?" + eInfo.TheTvDbId + ";poster;" + eInfo.Poster);
                    if(url != null && !url.equals("NONE")) {
                        WebGrabber.getFile("http://val.duckbox.info" + url, "converted/" + eInfo.TheTvDbId + "_poster.png");
                    }
                }
            }

            if(eInfo.Backdrop.length() > 0) {
                if(     new File("converted/" + eInfo.TheTvDbId + "_backdrop.m1v").isFile() == false ||
                        new File("converted/" + eInfo.TheTvDbId + "_backdrop_low.m1v").isFile() == false ||
                        new File("converted/" + eInfo.TheTvDbId + "_backdrop.png").isFile() == false) {
                    String url = WebGrabber.getText("http://val.duckbox.info/cgi-bin/convert.py?" + eInfo.TheTvDbId + ";backdrop;" + eInfo.Backdrop);
                    if(url != null && !url.equals("NONE")) {
                        String[] urls = url.split("<br />");
                        WebGrabber.getFile("http://val.duckbox.info" + urls[0], "converted/" + eInfo.TheTvDbId + "_backdrop.m1v");
                        WebGrabber.getFile("http://val.duckbox.info" + urls[1], "converted/" + eInfo.TheTvDbId + "_backdrop_low.m1v");
                        WebGrabber.getFile("http://val.duckbox.info" + urls[2], "converted/" + eInfo.TheTvDbId + "_backdrop.png");
                    }
                }
            }
        }
    }
}
