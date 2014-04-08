function slideDown(elem){
	//slide from 0 height
	elem.style.height = '0px';
	//show element, but cannot see it because it's height is 0
	show(elem);
	//get element's potential fullHeight
	var h = fullHeight(elem);
	//show a 20-frame animation within one sec
	for (var i = 0; i <= 100; i += 5) {
		//make sure i's closure function is right
		(function(){
			var pos = i;
			//set timeout and let it exec at the right time
			setTimeout(function(){
				//set the element's new height
				elem.style.height = (pos / 100) * h + "px";
			}, (pos + 1) * 10);//这里的触发时间为什么这样设置
		})();
	}
}

function fadeIn(elem){
	//从0透明度开始
	setOpacity(elem, 0);
	//显示元素，但是现在还看不见
	show(elem);
	//1秒钟内执行一个20帧的动画
	for(var i = 0;i < 100;i += 5){
		(function(){
			var pos = i;
			//设置timeout让它能在指定的时间间隔后运行
			setTimeout(function(){
				setOpacity(elem, pos);
			}, (pos + 1) * 10);
		})();
	}
}