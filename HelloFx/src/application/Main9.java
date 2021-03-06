package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

	
public class Main9 extends Application {
	TextField tf ;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = FXMLLoader.load(getClass().getResource("main9.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();	
			
			tf = (TextField) scene.lookup("#tf");
			Button btn1 = (Button) scene.lookup("#btn1");
			Button btn2 = (Button) scene.lookup("#btn2");
			Button btn3 = (Button) scene.lookup("#btn3");
			Button btn4 = (Button) scene.lookup("#btn4");
			Button btn5 = (Button) scene.lookup("#btn5");
			Button btn6 = (Button) scene.lookup("#btn6");
			Button btn7 = (Button) scene.lookup("#btn7");
			Button btn8 = (Button) scene.lookup("#btn8");
			Button btn9 = (Button) scene.lookup("#btn9");
			Button btn0 = (Button) scene.lookup("#btn0");
			Button btnCall = (Button) scene.lookup("#btnCall");
			
			btn1.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
//					String text1 = btn1.getText();
//					String tfResult = tf.getText();
//					tfResult += text1;
//					tf.setText(tfResult);
					click("1");
				}
			});
			btn2.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String text2 = btn2.getText();
					String tfResult = tf.getText();
					tfResult += text2;
					tf.setText(tfResult);
				}
			});
			btn3.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String text3 = btn3.getText();
					String tfResult = tf.getText();
					tfResult += text3;
					tf.setText(tfResult);
				}
			});
			btn4.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String text4 = btn4.getText();
					String tfResult = tf.getText();
					tfResult += text4;
					tf.setText(tfResult);
				}
			});
			btn5.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String text5 = btn5.getText();
					String tfResult = tf.getText();
					tfResult += text5;
					tf.setText(tfResult);
				}
			});
			btn6.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String text6 = btn6.getText();
					String tfResult = tf.getText();
					tfResult += text6;
					tf.setText(tfResult);
				}
			});
			btn7.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String text7 = btn7.getText();
					String tfResult = tf.getText();
					tfResult += text7;
					tf.setText(tfResult);
				}
			});
			btn8.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String text8 = btn8.getText();
					String tfResult = tf.getText();
					tfResult += text8;
					tf.setText(tfResult);
				}
			});
			btn9.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String text9 = btn9.getText();
					String tfResult = tf.getText();
					tfResult += text9;
					tf.setText(tfResult);
				}
			});
			btn0.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String text0 = btn0.getText();
					String tfResult = tf.getText();
					tfResult += text0;
					tf.setText(tfResult);
				}
			});
			btnCall.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String tfResult = tf.getText();
					String n1 = "";
					String n2 = "";
					String n3 = "";
					if(tfResult.length() > 9) {
						if(tfResult.substring(0,2).equals("01")) {
							n1 = tfResult.substring(0,3);
							n2 = tfResult.substring(3,7);
							n3 = tfResult.substring(7);
							tfResult = n1 + "-" + n2 + "-" + n3;
						}else if(tfResult.substring(0,2).equals("02")) {
							n1 = tfResult.substring(0,2);
							n2 = tfResult.substring(2,7);
							n3 = tfResult.substring(7);
							tfResult = n1 + "-" + n2 + "-" + n3;
						}else if(tfResult.substring(0,1).equals("0")) {
							n1 = tfResult.substring(0,3);
							n2 = tfResult.substring(3,6);
							n3 = tfResult.substring(6);
							tfResult = n1 + "-" + n2 + "-" + n3;
						}
					}
					Alert alert = new Alert(AlertType.INFORMATION);
					alert.setTitle("Calling...");
					alert.setHeaderText(null);
					alert.setContentText("Call to " + tfResult);
					
					alert.showAndWait();
				}
			});
		} catch(Exception e) {
			e.printStackTrace();
		}
		
	}
	
	public void click(String txt) {
//		Button temp = (Button) event.getTarget();
//		String txt = temp.getText();
		String tfResult = tf.getText();
		tf.setText(tfResult + txt);
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
