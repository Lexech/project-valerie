/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * Settings.java
 *
 * Created on 24.08.2009, 21:38:40
 */

package Gui;

import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;
import javax.swing.tree.DefaultMutableTreeNode;
import java.util.*;

/**
 *
 * @author Admin
 */
public class Settings extends javax.swing.JDialog {

    /** Creates new form Settings */
    public Settings(java.awt.Frame parent, boolean modal) {
        super(parent, modal);
        initComponents();

        for (int i = 0; i < jTree1  .getRowCount(); i++) {
            jTree1.expandRow(i);
        }

        jPanelGeneral.setVisible(true);
        jPanelConvert.setVisible(false);
        jPanelFileManagment.setVisible(false);
        jPanelImportManagment.setVisible(false);

        jLabelHeading.setText("General");

        jTextFieldFilter.setText(new valerie.tools.Properties().getPropertyString("FILTER_SERIES"));
    }

    /** This method is called from within the constructor to
     * initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is
     * always regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jSplitPaneApplyCancel = new javax.swing.JSplitPane();
        jButton1 = new javax.swing.JButton();
        jButton2 = new javax.swing.JButton();
        jSplitPaneTree = new javax.swing.JSplitPane();
        jLabel1 = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTree1 = new javax.swing.JTree();
        jLayeredPaneSettings = new javax.swing.JLayeredPane();
        jPanelGeneral = new javax.swing.JPanel();
        jCheckBox1 = new javax.swing.JCheckBox();
        jPanelFileManagment = new javax.swing.JPanel();
        jTextFieldFilter = new javax.swing.JTextField();
        jLabelFilter = new javax.swing.JLabel();
        jPanelImportManagment = new javax.swing.JPanel();
        jScrollPane2 = new javax.swing.JScrollPane();
        jTableImportManagment = new javax.swing.JTable();
        jButton3 = new javax.swing.JButton();
        jButton4 = new javax.swing.JButton();
        jPanelConvert = new javax.swing.JPanel();
        jCheckBoxResize = new javax.swing.JCheckBox();
        jLabel2 = new javax.swing.JLabel();
        jComboBoxEncoder = new javax.swing.JComboBox();
        jLabel3 = new javax.swing.JLabel();
        jComboBoxResolution = new javax.swing.JComboBox();
        jLabelHeading = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);
        org.jdesktop.application.ResourceMap resourceMap = org.jdesktop.application.Application.getInstance(valerie.ValerieApp.class).getContext().getResourceMap(Settings.class);
        setTitle(resourceMap.getString("Form.title")); // NOI18N
        setName("Form"); // NOI18N
        setResizable(false);
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowOpened(java.awt.event.WindowEvent evt) {
                SettingShow(evt);
            }
        });

        jSplitPaneApplyCancel.setBorder(null);
        jSplitPaneApplyCancel.setDividerSize(0);
        jSplitPaneApplyCancel.setName("jSplitPaneApplyCancel"); // NOI18N

        jButton1.setText(resourceMap.getString("jButtonApply.text")); // NOI18N
        jButton1.setName("jButtonApply"); // NOI18N
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });
        jSplitPaneApplyCancel.setLeftComponent(jButton1);

        jButton2.setText(resourceMap.getString("jButtonCancel.text")); // NOI18N
        jButton2.setName("jButtonCancel"); // NOI18N
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });
        jSplitPaneApplyCancel.setRightComponent(jButton2);

        jSplitPaneTree.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jSplitPaneTree.setDividerSize(1);
        jSplitPaneTree.setOrientation(javax.swing.JSplitPane.VERTICAL_SPLIT);
        jSplitPaneTree.setMinimumSize(new java.awt.Dimension(215, 45));
        jSplitPaneTree.setName("jSplitPaneTree"); // NOI18N
        jSplitPaneTree.setPreferredSize(new java.awt.Dimension(215, 45));

        jLabel1.setBackground(resourceMap.getColor("jLabel1.background")); // NOI18N
        jLabel1.setFont(new java.awt.Font("Arial", 1, 24));
        jLabel1.setForeground(resourceMap.getColor("jLabel1.foreground")); // NOI18N
        jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel1.setText(resourceMap.getString("jLabel1.text")); // NOI18N
        jLabel1.setHorizontalTextPosition(javax.swing.SwingConstants.CENTER);
        jLabel1.setMaximumSize(new java.awt.Dimension(215, 45));
        jLabel1.setMinimumSize(new java.awt.Dimension(215, 45));
        jLabel1.setName("jLabel1"); // NOI18N
        jLabel1.setOpaque(true);
        jLabel1.setPreferredSize(new java.awt.Dimension(215, 45));
        jSplitPaneTree.setTopComponent(jLabel1);

        jScrollPane1.setBackground(resourceMap.getColor("jScrollPane1.background")); // NOI18N
        jScrollPane1.setBorder(null);
        jScrollPane1.setName("jScrollPane1"); // NOI18N

        jTree1.setBackground(resourceMap.getColor("jTree1.background")); // NOI18N
        jTree1.setFont(resourceMap.getFont("jTree1.font")); // NOI18N
        javax.swing.tree.DefaultMutableTreeNode treeNode1 = new javax.swing.tree.DefaultMutableTreeNode("root");
        javax.swing.tree.DefaultMutableTreeNode treeNode2 = new javax.swing.tree.DefaultMutableTreeNode("General");
        treeNode1.add(treeNode2);
        treeNode2 = new javax.swing.tree.DefaultMutableTreeNode("File Managment");
        treeNode1.add(treeNode2);
        treeNode2 = new javax.swing.tree.DefaultMutableTreeNode("Convert");
        treeNode1.add(treeNode2);
        treeNode2 = new javax.swing.tree.DefaultMutableTreeNode("Movies");
        javax.swing.tree.DefaultMutableTreeNode treeNode3 = new javax.swing.tree.DefaultMutableTreeNode("Import Managment");
        treeNode2.add(treeNode3);
        treeNode1.add(treeNode2);
        treeNode2 = new javax.swing.tree.DefaultMutableTreeNode("TV");
        treeNode3 = new javax.swing.tree.DefaultMutableTreeNode("Import Managment");
        treeNode2.add(treeNode3);
        treeNode1.add(treeNode2);
        jTree1.setModel(new javax.swing.tree.DefaultTreeModel(treeNode1));
        jTree1.setLargeModel(true);
        jTree1.setName("jTree1"); // NOI18N
        jTree1.setRootVisible(false);
        jTree1.setRowHeight(30);
        jTree1.setShowsRootHandles(true);
        jTree1.addTreeSelectionListener(new javax.swing.event.TreeSelectionListener() {
            public void valueChanged(javax.swing.event.TreeSelectionEvent evt) {
                jTree1ValueChanged(evt);
            }
        });
        jScrollPane1.setViewportView(jTree1);

        jSplitPaneTree.setRightComponent(jScrollPane1);

        jLayeredPaneSettings.setBackground(resourceMap.getColor("jLayeredPaneSettings.background")); // NOI18N
        jLayeredPaneSettings.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jLayeredPaneSettings.setName("jLayeredPaneSettings"); // NOI18N
        jLayeredPaneSettings.setOpaque(true);

        jPanelGeneral.setName("jPanelGeneral"); // NOI18N
        jPanelGeneral.setOpaque(false);

        jCheckBox1.setText(resourceMap.getString("jCheckBox1.text")); // NOI18N
        jCheckBox1.setName("jCheckBox1"); // NOI18N
        jCheckBox1.setOpaque(false);

        javax.swing.GroupLayout jPanelGeneralLayout = new javax.swing.GroupLayout(jPanelGeneral);
        jPanelGeneral.setLayout(jPanelGeneralLayout);
        jPanelGeneralLayout.setHorizontalGroup(
            jPanelGeneralLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanelGeneralLayout.createSequentialGroup()
                .addContainerGap(36, Short.MAX_VALUE)
                .addComponent(jCheckBox1)
                .addGap(31, 31, 31))
        );
        jPanelGeneralLayout.setVerticalGroup(
            jPanelGeneralLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanelGeneralLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jCheckBox1)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        jPanelGeneral.setBounds(10, 70, 180, 30);
        jLayeredPaneSettings.add(jPanelGeneral, javax.swing.JLayeredPane.DEFAULT_LAYER);

        jPanelFileManagment.setName("jPanelFileManagment"); // NOI18N
        jPanelFileManagment.setOpaque(false);

        jTextFieldFilter.setText(resourceMap.getString("jTextFieldFilter.text")); // NOI18N
        jTextFieldFilter.setName("jTextFieldFilter"); // NOI18N

        jLabelFilter.setText(resourceMap.getString("jLabelFilter.text")); // NOI18N
        jLabelFilter.setName("jLabelFilter"); // NOI18N

        javax.swing.GroupLayout jPanelFileManagmentLayout = new javax.swing.GroupLayout(jPanelFileManagment);
        jPanelFileManagment.setLayout(jPanelFileManagmentLayout);
        jPanelFileManagmentLayout.setHorizontalGroup(
            jPanelFileManagmentLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanelFileManagmentLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabelFilter)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jTextFieldFilter, javax.swing.GroupLayout.DEFAULT_SIZE, 173, Short.MAX_VALUE)
                .addContainerGap())
        );
        jPanelFileManagmentLayout.setVerticalGroup(
            jPanelFileManagmentLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanelFileManagmentLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanelFileManagmentLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabelFilter)
                    .addComponent(jTextFieldFilter, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(109, Short.MAX_VALUE))
        );

        jPanelFileManagment.setBounds(10, 70, 270, 140);
        jLayeredPaneSettings.add(jPanelFileManagment, javax.swing.JLayeredPane.DEFAULT_LAYER);

        jPanelImportManagment.setBackground(resourceMap.getColor("jPanelImportManagment.background")); // NOI18N
        jPanelImportManagment.setName("jPanelImportManagment"); // NOI18N
        jPanelImportManagment.setOpaque(false);

        jScrollPane2.setBackground(resourceMap.getColor("jScrollPane2.background")); // NOI18N
        jScrollPane2.setName("jScrollPane2"); // NOI18N
        jScrollPane2.setOpaque(false);

        jTableImportManagment.setAutoCreateRowSorter(true);
        jTableImportManagment.setBackground(resourceMap.getColor("jTableImportManagment.background")); // NOI18N
        jTableImportManagment.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null}
            },
            new String [] {
                "Path"
            }
        ) {
            boolean[] canEdit = new boolean [] {
                false
            };

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        jTableImportManagment.setName("jTableImportManagment"); // NOI18N
        jTableImportManagment.setOpaque(false);
        jScrollPane2.setViewportView(jTableImportManagment);
        jTableImportManagment.getColumnModel().getColumn(0).setHeaderValue(resourceMap.getString("jTableImportManagment.columnModel.title0")); // NOI18N

        jButton3.setFont(resourceMap.getFont("jButton3.font")); // NOI18N
        jButton3.setText(resourceMap.getString("jButton3.text")); // NOI18N
        jButton3.setName("jButton3"); // NOI18N
        jButton3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton3ActionPerformed(evt);
            }
        });

        jButton4.setFont(resourceMap.getFont("jButton4.font")); // NOI18N
        jButton4.setText(resourceMap.getString("jButton4.text")); // NOI18N
        jButton4.setName("jButton4"); // NOI18N
        jButton4.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton4ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanelImportManagmentLayout = new javax.swing.GroupLayout(jPanelImportManagment);
        jPanelImportManagment.setLayout(jPanelImportManagmentLayout);
        jPanelImportManagmentLayout.setHorizontalGroup(
            jPanelImportManagmentLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanelImportManagmentLayout.createSequentialGroup()
                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 465, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanelImportManagmentLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(jButton4, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jButton3, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap())
        );
        jPanelImportManagmentLayout.setVerticalGroup(
            jPanelImportManagmentLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jScrollPane2, javax.swing.GroupLayout.DEFAULT_SIZE, 140, Short.MAX_VALUE)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanelImportManagmentLayout.createSequentialGroup()
                .addContainerGap(54, Short.MAX_VALUE)
                .addComponent(jButton4, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jButton3, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE))
        );

        jPanelImportManagment.setBounds(10, 70, 510, 140);
        jLayeredPaneSettings.add(jPanelImportManagment, javax.swing.JLayeredPane.DEFAULT_LAYER);

        jPanelConvert.setBackground(new java.awt.Color(250, 250, 250));
        jPanelConvert.setName("jPanelConvert"); // NOI18N

        jCheckBoxResize.setBackground(resourceMap.getColor("jCheckBoxResize.background")); // NOI18N
        jCheckBoxResize.setText(resourceMap.getString("jCheckBoxResize.text")); // NOI18N
        jCheckBoxResize.setHorizontalTextPosition(javax.swing.SwingConstants.LEADING);
        jCheckBoxResize.setName("jCheckBoxResize"); // NOI18N

        jLabel2.setText(resourceMap.getString("jLabel2.text")); // NOI18N
        jLabel2.setName("jLabel2"); // NOI18N

        jComboBoxEncoder.setModel(new javax.swing.DefaultComboBoxModel(new String[] { "mencoder", "jepg2yuv + mpeg2enc" }));
        jComboBoxEncoder.setName("jComboBoxEncoder"); // NOI18N

        jLabel3.setText(resourceMap.getString("jLabel3.text")); // NOI18N
        jLabel3.setName("jLabel3"); // NOI18N

        jComboBoxResolution.setModel(new javax.swing.DefaultComboBoxModel(new String[] { "1024x576 25fps", "1280x720 60fps", "1920x1080 60fps" }));
        jComboBoxResolution.setName("jComboBoxResolution"); // NOI18N

        javax.swing.GroupLayout jPanelConvertLayout = new javax.swing.GroupLayout(jPanelConvert);
        jPanelConvert.setLayout(jPanelConvertLayout);
        jPanelConvertLayout.setHorizontalGroup(
            jPanelConvertLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanelConvertLayout.createSequentialGroup()
                .addGroup(jPanelConvertLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanelConvertLayout.createSequentialGroup()
                        .addGap(106, 106, 106)
                        .addGroup(jPanelConvertLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(jLabel3)
                            .addComponent(jLabel2))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(jPanelConvertLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(jComboBoxResolution, 0, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jComboBoxEncoder, 0, 146, Short.MAX_VALUE)))
                    .addGroup(jPanelConvertLayout.createSequentialGroup()
                        .addGap(45, 45, 45)
                        .addComponent(jCheckBoxResize)))
                .addContainerGap(31, Short.MAX_VALUE))
        );
        jPanelConvertLayout.setVerticalGroup(
            jPanelConvertLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanelConvertLayout.createSequentialGroup()
                .addGap(12, 12, 12)
                .addComponent(jCheckBoxResize)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanelConvertLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jComboBoxEncoder, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel2))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanelConvertLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel3)
                    .addComponent(jComboBoxResolution, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(20, Short.MAX_VALUE))
        );

        jPanelConvert.setBounds(10, 70, 337, 108);
        jLayeredPaneSettings.add(jPanelConvert, javax.swing.JLayeredPane.DEFAULT_LAYER);

        jLabelHeading.setBackground(resourceMap.getColor("jLabelHeading.background")); // NOI18N
        jLabelHeading.setFont(resourceMap.getFont("jLabelHeading.font")); // NOI18N
        jLabelHeading.setForeground(resourceMap.getColor("jLabelHeading.foreground")); // NOI18N
        jLabelHeading.setLabelFor(jLayeredPaneSettings);
        jLabelHeading.setText(resourceMap.getString("jLabelHeading.text")); // NOI18N
        jLabelHeading.setVerticalAlignment(javax.swing.SwingConstants.BOTTOM);
        jLabelHeading.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jLabelHeading.setName("jLabelHeading"); // NOI18N
        jLabelHeading.setOpaque(true);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jSplitPaneTree, javax.swing.GroupLayout.PREFERRED_SIZE, 215, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jLabelHeading, javax.swing.GroupLayout.DEFAULT_SIZE, 528, Short.MAX_VALUE)
                    .addComponent(jLayeredPaneSettings, javax.swing.GroupLayout.DEFAULT_SIZE, 528, Short.MAX_VALUE)))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap(615, Short.MAX_VALUE)
                .addComponent(jSplitPaneApplyCancel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                        .addGap(7, 7, 7)
                        .addComponent(jLabelHeading, javax.swing.GroupLayout.PREFERRED_SIZE, 29, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jLayeredPaneSettings))
                    .addComponent(jSplitPaneTree, javax.swing.GroupLayout.PREFERRED_SIZE, 400, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jSplitPaneApplyCancel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jTree1ValueChanged(javax.swing.event.TreeSelectionEvent evt) {//GEN-FIRST:event_jTree1ValueChanged
        Object path[] = jTree1.getSelectionPaths()[0].getPath();

        String heading = "";
        for(int i = 1; i < path.length; i++) {
            heading += ((DefaultMutableTreeNode)path[i]).getUserObject();
            
            if(i+1 < path.length)
                heading += " : ";
        }

        jLabelHeading.setText(heading);

        if(((DefaultMutableTreeNode)path[1]).getUserObject().equals("General")) {
            jPanelGeneral.setVisible(true);
            jPanelFileManagment.setVisible(false);
            jPanelConvert.setVisible(false);
            jPanelImportManagment.setVisible(false);
        } else if(((DefaultMutableTreeNode)path[1]).getUserObject().equals("File Managment")) {
            jPanelFileManagment.setVisible(true);
            jPanelGeneral.setVisible(false);
            jPanelConvert.setVisible(false);
            jPanelImportManagment.setVisible(false);
        } else if(((DefaultMutableTreeNode)path[1]).getUserObject().equals("Convert")) {
            jPanelFileManagment.setVisible(false);
            jPanelGeneral.setVisible(false);
            jPanelConvert.setVisible(true);
            jPanelImportManagment.setVisible(false);

            jCheckBoxResize.setSelected(new valerie.tools.Properties().getPropertyBoolean("RESIZE_BACKDROP"));
            jComboBoxEncoder.setSelectedIndex(new valerie.tools.Properties().getPropertyInt("ENCODER_TYPE"));
            jComboBoxResolution.setSelectedIndex(new valerie.tools.Properties().getPropertyInt("RESOLUTION_TYPE"));

        } else if(path.length == 1) {

        } else if(((DefaultMutableTreeNode)path[1]).getUserObject().equals("Movies") && ((DefaultMutableTreeNode)path[2]).getUserObject().equals("Import Managment")) {
            jPanelImportManagment.setVisible(true);
            jPanelGeneral.setVisible(false);
            jPanelFileManagment.setVisible(false);
            jPanelConvert.setVisible(false);

            String[] pathsMovies = WorkPathMovies.split("\\|");
            ((DefaultTableModel) jTableImportManagment.getModel()).setRowCount(pathsMovies.length);

            //String[] pathsMovies = new valerie.tools.Properties().getPropertyString("PATHS_MOVIES").split("\\|");
            //((DefaultTableModel) jTableImportManagment.getModel()).setRowCount(pathsMovies.length);

            int iteratorMovies = 0;
            for(String pathMovies : pathsMovies) {
                    jTableImportManagment.setValueAt(pathMovies, iteratorMovies++, 0);
            }
        } else if(((DefaultMutableTreeNode)path[1]).getUserObject().equals("TV") && ((DefaultMutableTreeNode)path[2]).getUserObject().equals("Import Managment")) {
            jPanelImportManagment.setVisible(true);
            jPanelGeneral.setVisible(false);
            jPanelFileManagment.setVisible(false);
            jPanelConvert.setVisible(false);

            String[] pathsMovies = WorkPathTV.split("\\|");
            ((DefaultTableModel) jTableImportManagment.getModel()).setRowCount(pathsMovies.length);

            //String[] pathsMovies = new valerie.tools.Properties().getPropertyString("PATHS_SERIES").split("\\|");
            //((DefaultTableModel) jTableImportManagment.getModel()).setRowCount(pathsMovies.length);

            int iteratorMovies = 0;
            for(String pathMovies : pathsMovies) {
                    jTableImportManagment.setValueAt(pathMovies, iteratorMovies++, 0);
            }
        }
    }//GEN-LAST:event_jTree1ValueChanged

    private void jButton4ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton4ActionPerformed
        //valerie.tools.Properties prop = new valerie.tools.Properties();

        String pathToAdd = JOptionPane.showInputDialog("New Directory:");
        if(pathToAdd != null && pathToAdd.length() > 0) {
            Object path[] = jTree1.getSelectionPaths()[0].getPath();
            if(((DefaultMutableTreeNode)path[1]).getUserObject().equals("Movies") && ((DefaultMutableTreeNode)path[2]).getUserObject().equals("Import Managment")) {
                //String paths = prop.getPropertyString("PATHS_MOVIES");
                
                if(!WorkPathMovies.contains(pathToAdd))
                    WorkPathMovies +=(pathToAdd + "|");

                //if(!paths.contains(pathToAdd))
                //    prop.setProperty("PATHS_MOVIES", paths + pathToAdd + "|");

            } else if(((DefaultMutableTreeNode)path[1]).getUserObject().equals("TV") && ((DefaultMutableTreeNode)path[2]).getUserObject().equals("Import Managment")) {
                //String paths = prop.getPropertyString("PATHS_SERIES");

                if(!WorkPathTV.contains(pathToAdd))
                    WorkPathTV += (pathToAdd + "|");

                //if(!paths.contains(pathToAdd))
                //    prop.setProperty("PATHS_SERIES", paths + pathToAdd + "|");
            }
        }

        //prop.save();

        jTree1ValueChanged(null);
    }//GEN-LAST:event_jButton4ActionPerformed

    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton3ActionPerformed
        //valerie.tools.Properties prop = new valerie.tools.Properties();

        Object path[] = jTree1.getSelectionPaths()[0].getPath();
        if(((DefaultMutableTreeNode)path[1]).getUserObject().equals("Movies") && ((DefaultMutableTreeNode)path[2]).getUserObject().equals("Import Managment")) {
            String pathToDelete = jTableImportManagment.getValueAt(jTableImportManagment.getSelectedRow(), jTableImportManagment.getSelectedColumn()).toString();

            WorkPathMovies = WorkPathMovies.replaceAll(pathToDelete + "\\|", "");

            //String paths = prop.getPropertyString("PATHS_MOVIES");
            //paths = paths.replaceAll(pathToDelete + "\\|", "");

            //prop.setProperty("PATHS_MOVIES", paths);

        } else if(((DefaultMutableTreeNode)path[1]).getUserObject().equals("TV") && ((DefaultMutableTreeNode)path[2]).getUserObject().equals("Import Managment")) {
            String pathToDelete = jTableImportManagment.getValueAt(jTableImportManagment.getSelectedRow(), jTableImportManagment.getSelectedColumn()).toString();

            WorkPathTV = WorkPathTV.replaceAll(pathToDelete + "\\|", "");

            //String paths = prop.getPropertyString("PATHS_SERIES");
            //paths = paths.replaceAll((pathToDelete + "\\|"), "");

            //prop.setProperty("PATHS_SERIES", paths);
        }

        //prop.save();

        jTree1ValueChanged(null);
    }//GEN-LAST:event_jButton3ActionPerformed

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        valerie.tools.Properties prop = new valerie.tools.Properties();
        prop.setProperty("FILTER_MOVIES", jTextFieldFilter.getText());
        prop.setProperty("FILTER_SERIES", jTextFieldFilter.getText());
        prop.setProperty("RESIZE_BACKDROP", new Boolean(jCheckBoxResize.isSelected()).toString());
        prop.setProperty("ENCODER_TYPE",Integer.toString(jComboBoxEncoder.getSelectedIndex()));
        prop.setProperty("RESOLUTION_TYPE",Integer.toString(jComboBoxResolution.getSelectedIndex()));
        prop.setProperty("PATHS_MOVIES", WorkPathMovies);
        prop.setProperty("PATHS_SERIES", WorkPathTV);
        prop.save();
        setVisible(false);
    }//GEN-LAST:event_jButton1ActionPerformed

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        setVisible(false);
    }//GEN-LAST:event_jButton2ActionPerformed

    private void SettingShow(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_SettingShow
        WorkPathMovies = new valerie.tools.Properties().getPropertyString("PATHS_MOVIES");
        WorkPathTV = new valerie.tools.Properties().getPropertyString("PATHS_SERIES");
    }//GEN-LAST:event_SettingShow

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton3;
    private javax.swing.JButton jButton4;
    private javax.swing.JCheckBox jCheckBox1;
    private javax.swing.JCheckBox jCheckBoxResize;
    private javax.swing.JComboBox jComboBoxEncoder;
    private javax.swing.JComboBox jComboBoxResolution;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabelFilter;
    private javax.swing.JLabel jLabelHeading;
    private javax.swing.JLayeredPane jLayeredPaneSettings;
    private javax.swing.JPanel jPanelConvert;
    private javax.swing.JPanel jPanelFileManagment;
    private javax.swing.JPanel jPanelGeneral;
    private javax.swing.JPanel jPanelImportManagment;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JSplitPane jSplitPaneApplyCancel;
    private javax.swing.JSplitPane jSplitPaneTree;
    private javax.swing.JTable jTableImportManagment;
    private javax.swing.JTextField jTextFieldFilter;
    private javax.swing.JTree jTree1;
    // End of variables declaration//GEN-END:variables
    private String WorkPathMovies;
    private String WorkPathTV;
}
