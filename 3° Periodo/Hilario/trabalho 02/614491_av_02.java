package teste;

import javax.swing.JOptionPane;

class Pessoa{
    private String nome;
    private String dia;
    private String mes;
    private String ano;
    private double altura;


    public void setNome(String nome){
        this.nome = nome;
    }

    public void setData(String dia){
        this.dia = dia;
    }
    
    public void setMes(String mes) {
    	this.mes = mes;
    }
    
    public void setAno(String ano) {
    	this.ano = ano;
    }

    public void setAltura(double altura){
        this.altura = altura;
    }

    public void getNome(){
        JOptionPane.showMessageDialog(null ,"Seu nome -> "+nome);
    }

    public void getData(){
        JOptionPane.showMessageDialog(null ,""+dia+"/"+mes+"/"+ano);
    }

    public void getAltura(){
        JOptionPane.showMessageDialog(null ,"Sua altura ->"+altura);
    }
    
    public static void main(String[] args){
        Pessoa obj1 = new Pessoa();

        String nome = JOptionPane.showInputDialog("Digite o nome! ");
        
        obj1.setNome(nome);
        obj1.getNome();
        
        String data = JOptionPane.showInputDialog("Dia ");
        String mes = JOptionPane.showInputDialog("Mes ");
        String ano = JOptionPane.showInputDialog("Ano ");
        
        obj1.setData(data);
        obj1.setMes(mes);
        obj1.setAno(ano);
        obj1.getData();
        
        double altura = Double.parseDouble(JOptionPane.showInputDialog("Digite sua altura"));
        
        obj1.setAltura(altura);
        obj1.getAltura();
        

    }
}