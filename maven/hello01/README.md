# How to create a minimal Java jar executable. 

## Use the pom.xml

```xml
<project>
 <modelVersion>4.0.0</modelVersion>
 <groupId>local.Hello</groupId>
 <artifactId>hello</artifactId>
 <version>1.0</version>
 <build>
    <pluginManagement>
        <plugins>
            <!-- Default java version was 1.5, to change the default version added this plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
        </plugins>
    </pluginManagement>
</build>
</project>
```

## Add main class

Location
```bash
src/main/java/local/Hello/Main.java
```

Code
```java
package local.Hello;
public class Main {
  public static void main(String[] args) {
    System.out.println("Hello world");
  }
}
```

## To create jar
```bash
mvn package
```

## To run
```bash
$ java -cp target/hello-1.0.jar local.Hello.Main
Hello world
```

## View the Manifesto and files in the jar
```bash
$ jar -tvxf target/hello-1.0.jar
```
