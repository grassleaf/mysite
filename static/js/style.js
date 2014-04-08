//获取指定元素（elem）的样式属性（name
function getStyle(elem, name){
	//如果属性存在与style[]中，那它已经被设置了（并且是当前的）
	if (elem.style[name]) 
		return elem.style[name];
	//否则尝试使用IE的方法
	else if (elem.currentStyle)
		return elem.currentStyle[name];
	//或者使用W3C的方法
	else if (document.defaultView && document.defaultView.getComputedStyle) {
		//它使用的是通用的'text-align'的样式规则而非'textAlign'
		name = name.replace(/([A-Z])/g,"-$1");
		name = name.toLowerCase();
		//获取样式对象并获取属性值
		var s = document.defaultView.getComputedStyle(elem, "");
		return s && s.getPropertyValue(name);
	} else 
		return null;
}

/*和位置相关的函数*/


/*和尺寸相关的函数*/

//获取元素的真实高度（使用CSS最终样式值）
function getHeight(elem){
	//获取CSS的最终值并解析出可用的数值
	return parseInt(getStyle(elem, 'height'));
}

//查找元素完整、可能的高度
function fullHeight(elem){
	//如果元素是显示的，那么使用offsetHeight就能得到高度，如果没有offsetHeight，则使用getHeight()
	if (getStyle(elem, 'display') != 'none') 
		return elem.offsetHeight || getHeight(elem);
	//否则我们必须处理display为none的元素，重置它的CSS属性以获取更精确的读数
	var old = resetCSS(elem, {
		display: '',
		visibility: 'hidden',
		position: 'absolute'
	});
	//使用clientHeight找出元素的完整高度，如果还不生效，则使用getHeight函数
	var h = elem.clientHeight || getHeight(elem);
	//恢复CSS的原有属性
	restoreCSS(elem);
	//返回元素的完整高度
	return h;
}

//设置CSS一组属性的函数，它可以恢复到原有设置
function resetCSS(elem, prop){
	var old = {};
	for (var i = i in prop) {
		//记录旧的属性值
		old[i] = elem.style[i];
		//设置新属性值
		elem.style[i] = prop[i];
	}
	//返回旧属性值以备恢复
	return old;
}

//恢复CSS原有属性
function restoreCSS(elem, prop){
	for (var i = i in prop) {
		elem.style[i] = prop[i];
	}
}

/*和可见性相关的函数*/

//使用display显示元素的函数
function show(elem){
	//设置display属性为它的原始值，如没有记录有原始值，则使用'block'
	elem.style.display = elem.$oldDisplay || '';
}

//设置元素透明度的函数
function setOpacity(elem, level){
	//如果存在filters这个属性，则它是IE，所以设置元素的Align滤镜
	if(elem.filters)
		elem.style.filters = 'alpha(opacity=' + level + ')';
	//否则使用W3C的opacity属性
	else
		elem.style.opacity = level / 100;
}