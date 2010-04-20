/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * Console.java
 *
 * Created on 17.04.2010, 11:24:46
 */

package Gui;

import java.awt.Point;
import org.jdesktop.application.Action;
import valerie.tools.DebugOutput;

/**
 *
 * @author i7
 */
public class Console extends javax.swing.JFrame {

    /** Creates new form Console */
    public Console(java.awt.Frame parent, boolean modal) {
        initComponents();

        DebugOutput.add(new DebugOutput.OutputHandler() {
            @Override
            public void print(String s) {
                jTextAreaConsole.append(s);
                jTextAreaConsole.setCaretPosition(jTextAreaConsole.getText().length());
            }
        }
        );
    }

    /** This method is called from within the constructor to
     * initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is
     * always regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jScrollPaneConsole = new javax.swing.JScrollPane();
        jTextAreaConsole = new javax.swing.JTextArea();
        jPanelTop = new javax.swing.JPanel();
        jButtonClear = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);
        org.jdesktop.application.ResourceMap resourceMap = org.jdesktop.application.Application.getInstance(valerie.ValerieApp.class).getContext().getResourceMap(Console.class);
        setTitle(resourceMap.getString("Console.title")); // NOI18N
        setMinimumSize(new java.awt.Dimension(800, 800));
        setName("Console"); // NOI18N

        jScrollPaneConsole.setVerticalScrollBarPolicy(javax.swing.ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        jScrollPaneConsole.setName("jScrollPaneConsole"); // NOI18N

        jTextAreaConsole.setColumns(20);
        jTextAreaConsole.setEditable(false);
        jTextAreaConsole.setRows(5);
        jTextAreaConsole.setName("jTextAreaConsole"); // NOI18N
        jScrollPaneConsole.setViewportView(jTextAreaConsole);

        getContentPane().add(jScrollPaneConsole, java.awt.BorderLayout.CENTER);

        jPanelTop.setName("jPanelTop"); // NOI18N
        jPanelTop.setLayout(new java.awt.BorderLayout());

        javax.swing.ActionMap actionMap = org.jdesktop.application.Application.getInstance(valerie.ValerieApp.class).getContext().getActionMap(Console.class, this);
        jButtonClear.setAction(actionMap.get("clear")); // NOI18N
        jButtonClear.setText(resourceMap.getString("jButtonClear.text")); // NOI18N
        jButtonClear.setName("jButtonClear"); // NOI18N
        jPanelTop.add(jButtonClear, java.awt.BorderLayout.CENTER);

        getContentPane().add(jPanelTop, java.awt.BorderLayout.PAGE_START);

        pack();
    }// </editor-fold>//GEN-END:initComponents

    @Action
    public void clear() {
        jTextAreaConsole.setText("");
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButtonClear;
    private javax.swing.JPanel jPanelTop;
    private javax.swing.JScrollPane jScrollPaneConsole;
    private javax.swing.JTextArea jTextAreaConsole;
    // End of variables declaration//GEN-END:variables

}