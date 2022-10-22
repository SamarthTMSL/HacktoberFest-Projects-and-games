import 'react-native-gesture-handler';
import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator} from '@react-navigation/stack';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { Ionicons} from '@expo/vector-icons';
import { Provider } from 'react-redux';

import FavoritesScreen from './screens/FavoritesScreen';
import CategoriesScreen from './screens/CategoriesScreen';
import MealsOverviewScreen from './screens/MealsOverviewScreen';
import MealDetailScreen from './screens/MealDetailScreen';
import FavoritesContextProvider from './store/context/favorites-context';
import { store } from './store/redux/store';

const Stack = createStackNavigator();
const Drawer = createDrawerNavigator();

function DrawerNavigator() {
  return (<Drawer.Navigator
    screenOptions={{
      headerStyle: { backgroundColor: '#351401'},
      headerTintColor: 'white',
      sceneContainerStyle: { backgroundColor: '#3f2f25'},
      drawerContentStyle: { backgroundColor: '#351401'},
      drawerInactiveTintColor: 'white',
      drawerActiveTintColor: '#351401',
      drawerActiveBackgroundColor: '#e4baa1'
    }}
  >
    <Drawer.Screen name='Categories' component={CategoriesScreen} options={{
      title: 'All Categories',
      drawerIcon: ({color, size}) => (
      <Ionicons name='list' color={color} size={size}/>
      ),
    }}/>
    <Drawer.Screen name='Favorites' component={FavoritesScreen} options={{
      drawerIcon: ({color, size}) => (
        <Ionicons name='star' color={color} size={size}/>
        ),
    }}/>
  </Drawer.Navigator>);
}

export default function App() {
  return (
    <>
    <StatusBar style='light' />
    {/* <FavoritesContextProvider> */}
    <Provider store={store}>
    <NavigationContainer>
      <Stack.Navigator
      screenOptions={{
        headerStyle: { backgroundColor: '#351401'},
        headerTintColor: 'white',
        cardStyle: { backgroundColor: '#3f2f25'}
      }}
      >
        <Stack.Screen name="Drawer" 
        component={DrawerNavigator} 
        options={{
        headerShown: false,
        }}/>
        <Stack.Screen 
        name="MealsOverview" 
        component={MealsOverviewScreen}
        // options={({ route, navigation }) => {
        //   const catId = route.params.categoryId;
        //   return {
        //     title: catId,
        //   };
        // }}
        />
        <Stack.Screen
        name='MealDetail'
        component={MealDetailScreen}
        // options={{
        //   headerRight: () => {
        //     return <Button title='Tap me!'/>
        //   },
        // }}
        options={{
          title: 'About the Meal'
        }}
        />
        
      </Stack.Navigator>
    </NavigationContainer>
    </Provider>
    {/* </FavoritesContextProvider> */}
    
    
    
    </>
   
  );
}

const styles = StyleSheet.create({
  container: {
    
  },
});
